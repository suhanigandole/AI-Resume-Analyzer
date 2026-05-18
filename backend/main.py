# This connects everything

from fastapi import FastAPI, UploadFile, Form
import pdfplumber
from docx import Document

app = FastAPI()

def extract_text(file: UploadFile):
    filename = file.filename.lower()
    text = ""

    try:
        if filename.endswith(".pdf"):
            with pdfplumber.open(file.file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text

        elif filename.endswith(".docx"):
            doc = Document(file.file)
            text = "\n".join([p.text for p in doc.paragraphs])

        return text.strip()

    except:
        return ""
    

@app.post("/analyze")
def analyze(resume: UploadFile, job_desc: str = Form(...)):

    text = extract_text(resume)

    # SAFE CHECK (THIS PREVENTS 500 ERROR)
    if not text:
        return {
            "error": "Could not read resume file. Try another PDF/DOCX."
        }

    # SIMPLE DUMMY SCORE (so project ALWAYS runs)
    score = 70

    if "python" in job_desc.lower():
        score += 10
    if "fastapi" in job_desc.lower():
        score += 10

    return {
        "ats_score": min(score, 100),
        "match_level": "Medium Match"
    }
   
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)