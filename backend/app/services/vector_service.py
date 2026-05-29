import chromadb

from sentence_transformers import SentenceTransformer

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="video_chunks"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def store_video_chunks(
    transcript: str,
    video_id: str
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(
        transcript
    )

    embeddings = embedding_model.encode(
        chunks
    )

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[
                f"{video_id}_{i}"
            ],
            documents=[
                chunk
            ],
            embeddings=[
                embeddings[i].tolist()
            ],
            metadatas=[
                {
                    "video_id": video_id,
                    "chunk_id": i
                }
            ]
        )

    return len(chunks)

def search_chunks(
    query: str,
    top_k: int = 5
):

    query_embedding = (
        embedding_model
        .encode(query)
        .tolist()
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results