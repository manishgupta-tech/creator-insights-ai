from app.services.vector_service import (
    search_chunks
)

from app.services.gemini_service import (
    ask_gemini
)

# ==========================
# SIMPLE MEMORY
# ==========================
chat_memory = []


def answer_question(
    question: str
):

    global chat_memory

    results = search_chunks(
        question
    )

    docs = results["documents"][0]

    context = "\n\n".join(
        docs
    )

    memory_context = "\n".join(
        chat_memory[-5:]
    )

    prompt = f"""
You are an AI creator analyst.

Previous Conversation:
{memory_context}

Retrieved Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_gemini(
        prompt
    )

    chat_memory.append(
        f"User: {question}"
    )

    chat_memory.append(
        f"Assistant: {answer}"
    )

    return {
        "answer": answer,
        "sources": results["metadatas"][0]
    }