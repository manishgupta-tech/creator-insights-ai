from fastapi import APIRouter
from app.services.gemini_service import ask_gemini
from app.services.vector_service import (
    search_chunks
)

from app.services.rag_service import (
    answer_question
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

@router.post("/ask")
def ask(data: dict):

    question = data["question"]

    return answer_question(
        question
    )