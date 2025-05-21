from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    filetype = Column(String)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
    extracted_text = Column(Text)

# Table creation block (run only if this file is executed directly)
if __name__ == "__main__":
    from app.core.database import engine
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")
