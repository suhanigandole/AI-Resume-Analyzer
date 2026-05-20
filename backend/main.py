from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
from docx import Document

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Extract Resume Text
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

# Analyze API
@app.post("/analyze")
def analyze(resume: UploadFile, job_desc: str = Form(...)):

    # File Validation
    if not (
        resume.filename.endswith(".pdf")
        or resume.filename.endswith(".docx")
    ):
        return {
            "error": "Only PDF or DOCX files allowed"
        }

    text = extract_text(resume)

    if not text:
        return {
            "error": "Could not read resume"
        }

    # Dummy ATS Logic
    score = 70

    if "python" in job_desc.lower():
        score += 10

    if "fastapi" in job_desc.lower():
        score += 10

    if "sql" in job_desc.lower():
        score += 5

    score = min(score, 100)

    # Match Level
    if score >= 80:
        level = "Strong Match"
    elif score >= 50:
        level = "Medium Match"
    else:
        level = "Weak Match"

    return {
        "ats_score": score,
        "match_level": level
    }