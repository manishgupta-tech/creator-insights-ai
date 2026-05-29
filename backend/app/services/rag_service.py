from app.services.vector_service import (
    search_chunks
)

from app.services.gemini_service import (
    ask_gemini
)


def answer_question(
    question: str
):

    results = search_chunks(
        question
    )

    docs = results["documents"][0]

    context = "\n\n".join(
        docs
    )

    prompt = f"""
You are an AI creator analyst.

Use the provided context to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_gemini(
        prompt
    )

    return {
        "answer": answer,
        "sources": results["metadatas"][0]
    }