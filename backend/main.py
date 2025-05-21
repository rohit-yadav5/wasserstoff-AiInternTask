from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not present
nltk.download('vader_lexicon', quiet=True)

app = FastAPI()

# --- CORS Middleware (MUST be before endpoints) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],  # Add "*" for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sia = SentimentIntensityAnalyzer()
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

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

        sentiment_scores = sia.polarity_scores(extracted_text)

        return JSONResponse(
            content={
                "filename": file.filename,
                "message": "File uploaded and text extracted successfully!",
                "extracted_text": extracted_text,
                "sentiment": sentiment_scores
            }
        )
    except Exception as e:
        return JSONResponse(
            content={
                "message": f"Error: {str(e)}",
                "filename": getattr(file, 'filename', 'unknown'),
                "extracted_text": "",
                "sentiment": {}
            },
            status_code=500
        )
