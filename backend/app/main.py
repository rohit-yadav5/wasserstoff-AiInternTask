import os
import datetime
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from app.models.document import Document, Base
from app.core.database import SessionLocal, engine

# NLTK setup
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Upload directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.normpath(os.path.join(BASE_DIR, '../../data/uploaded_files'))
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- DOCUMENT ENDPOINTS ---

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # OCR extraction
    extracted_text = ""
    if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(file_location)
        extracted_text = pytesseract.image_to_string(image)
    elif file.filename.lower().endswith('.pdf'):
        images = convert_from_path(file_location)
        for img in images:
            extracted_text += pytesseract.image_to_string(img)
    else:
        return JSONResponse(
            content={
                "message": "Unsupported file type.",
                "filename": file.filename,
                "extracted_text": "",
                "sentiment": {}
            },
            status_code=400
        )

    # Sentiment analysis
    sentiment_scores = sia.polarity_scores(extracted_text)

    # Save document to DB (store sentiment as string)
    doc = Document(
        filename=file.filename,
        filetype=file.filename.split('.')[-1],
        extracted_text=extracted_text,
        upload_time=datetime.datetime.utcnow(),
        sentiment=str(sentiment_scores)
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return JSONResponse(
        content={
            "filename": file.filename,
            "message": "File uploaded and text extracted successfully!",
            "extracted_text": extracted_text,
            "sentiment": sentiment_scores,
            "document_id": doc.id
        }
    )

@app.get("/documents/")
def list_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    return [
        {
            "id": doc.id,
            "filename": doc.filename,
            "filetype": doc.filetype,
            "upload_time": doc.upload_time,
        }
        for doc in docs
    ]

@app.get("/documents/{doc_id}")
def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    # Convert sentiment string back to dict if needed
    try:
        import ast
        sentiment = ast.literal_eval(doc.sentiment) if doc.sentiment else {}
    except Exception:
        sentiment = {}
    return {
        "id": doc.id,
        "filename": doc.filename,
        "filetype": doc.filetype,
        "upload_time": doc.upload_time,
        "extracted_text": doc.extracted_text,
        "sentiment": sentiment,
    }

@app.delete("/documents/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    file_path = os.path.join(UPLOAD_DIR, doc.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    db.delete(doc)
    db.commit()
    return {"message": f"Document {doc_id} deleted successfully"}

@app.get("/documents/{doc_id}/download")
def download_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    file_path = os.path.join(UPLOAD_DIR, doc.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on disk")
    return FileResponse(file_path, filename=doc.filename)

@app.get("/health")
def health():
    return {"status": "ok"}
