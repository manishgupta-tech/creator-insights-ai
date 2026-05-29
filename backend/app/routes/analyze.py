from fastapi import APIRouter
from app.services.youtube_service import (
    get_youtube_metadata,
    get_youtube_transcript
)

router = APIRouter()


@router.post("/analyze-youtube")
def analyze_youtube(data: dict):

    url = data["youtube_url"]

    metadata = get_youtube_metadata(url)

    transcript = get_youtube_transcript(url)

    return {
        "metadata": metadata,
        "transcript_preview": transcript[:1000]
    }