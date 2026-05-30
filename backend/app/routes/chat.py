from fastapi import APIRouter

from app.services.gemini_service import ask_gemini

from app.services.vector_service import (
    search_chunks
)

from app.services.rag_service import (
    answer_question
)

router = APIRouter()


# ==========================
# TEST GEMINI
# ==========================
@router.get("/test-ai")
def test_ai():

    result = ask_gemini(
        "Explain RAG in one sentence."
    )

    return {
        "response": result
    }


# ==========================
# TEST VECTOR SEARCH
# ==========================
@router.get("/test-search")
def test_search():

    results = search_chunks(
        "What is this video about?"
    )

    return results


# ==========================
# NORMAL RAG CHAT
# ==========================
@router.post("/ask")
def ask(data: dict):

    question = data["question"]

    return answer_question(
        question
    )


# ==========================
# VIDEO COMPARISON
# ==========================
@router.post("/compare")
def compare_videos(data: dict):

    question = data["question"]

    comparison_prompt = f"""
You are a creator growth expert.

Compare Video A and Video B.

Question:
{question}

Use transcript chunks from both videos.

Provide:
1. Key differences
2. Hook comparison
3. Content comparison
4. Improvement suggestions
"""

    return answer_question(
        comparison_prompt
    )