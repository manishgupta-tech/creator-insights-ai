from fastapi import APIRouter
from app.services.gemini_service import ask_gemini
from app.services.vector_service import (
    search_chunks
)

router = APIRouter()

@router.get("/test-ai")
def test_ai():

    result = ask_gemini(
        "Explain RAG in one sentence."
    )

    return {
        "response": result
    }

@router.get("/test-search")
def test_search():

    results = search_chunks(
        "What is this video about?"
    )

    return results