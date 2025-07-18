from fastapi import APIRouter, UploadFile, Form
from ..utils.resume_parser import parse_pdf, parse_docx
from ..services.llm_service import analyze_resume

router = APIRouter()


@router.post("/analyze")
async def analyze(file: UploadFile, job_desc: str = Form(...)):
    if file.filename.endswith(".pdf"):
        content = parse_pdf(file.file)
    elif file.filename.endswith(".docx"):
        content = parse_docx(file.file)
    else:
        return {"error": "Unsupported file type"}

    result = analyze_resume(content, job_desc)
    return {"analysis": result}
