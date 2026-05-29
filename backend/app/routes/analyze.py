from fastapi import APIRouter

from app.services.youtube_service import (
    get_youtube_metadata,
    get_youtube_transcript
)

from app.services.instagram_service import (
    get_instagram_metadata
)

from app.services.vector_service import (
    store_video_chunks
)

router = APIRouter()


# ==========================
# YOUTUBE ANALYSIS
# ==========================
@router.post("/analyze-youtube")
def analyze_youtube(data: dict):

    url = data["youtube_url"]

    metadata = get_youtube_metadata(url)

    transcript = get_youtube_transcript(url)

    chunks_saved = store_video_chunks(
        transcript,
        "A"
    )

    return {
        "metadata": metadata,
        "chunks_saved": chunks_saved,
        "transcript_preview": transcript[:1000]
    }


# ==========================
# INSTAGRAM ANALYSIS
# ==========================
@router.post("/analyze-instagram")
def analyze_instagram(data: dict):

    url = data["instagram_url"]

    metadata = get_instagram_metadata(url)

    return {
        "metadata": metadata
    }


# ==========================
# COMBINED ANALYSIS
# ==========================
@router.post("/analyze")
def analyze_videos(data: dict):

    youtube_url = data["youtube_url"]
    instagram_url = data["instagram_url"]

    youtube_metadata = get_youtube_metadata(
        youtube_url
    )

    youtube_transcript = get_youtube_transcript(
        youtube_url
    )

    youtube_chunks = store_video_chunks(
    youtube_transcript,
    "A"
    )

    instagram_metadata = get_instagram_metadata(
        instagram_url
    )

    return {
        "video_a": {
            "metadata": youtube_metadata,
            "transcript_preview": youtube_transcript[:1000],
            "chunks_saved": youtube_chunks
        },
        "video_b": {
            "metadata": instagram_metadata
        }
    }