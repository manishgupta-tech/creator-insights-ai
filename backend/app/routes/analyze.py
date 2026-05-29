from fastapi import APIRouter

from app.services.youtube_service import (
    get_youtube_metadata,
    get_youtube_transcript
)

from app.services.instagram_service import (
    get_instagram_metadata
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

    return {
        "metadata": metadata,
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

    instagram_metadata = get_instagram_metadata(
        instagram_url
    )

    return {
        "video_a": {
            "metadata": youtube_metadata,
            "transcript_preview": youtube_transcript[:1000]
        },
        "video_b": {
            "metadata": instagram_metadata
        }
    }