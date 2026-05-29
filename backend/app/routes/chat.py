from fastapi import APIRouter
from app.services.gemini_service import ask_gemini

router = APIRouter()

@router.get("/test-ai")
def test_ai():

    result = ask_gemini(
        "Explain RAG in one sentence."
    )

    return {
        "response": result
    }