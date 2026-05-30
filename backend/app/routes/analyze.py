from fastapi import APIRouter

from app.services.youtube_service import (
    get_youtube_metadata,
    get_youtube_transcript
)

from app.services.instagram_service import (
    get_instagram_metadata,
    get_instagram_transcript
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
# TWO VIDEO ANALYSIS
# ==========================
@router.post("/analyze")
def analyze_videos(data: dict):

    video_a_url = data["video_a_url"]
    video_b_url = data["video_b_url"]

    # ==========================
    # VIDEO A
    # ==========================
    metadata_a = get_youtube_metadata(
        video_a_url
    )

    transcript_a = get_youtube_transcript(
        video_a_url
    )

    chunks_a = store_video_chunks(
        transcript_a,
        "A"
    )

    engagement_a = round(
        (
            (
                metadata_a.get("likes", 0)
                +
                metadata_a.get("comments", 0)
            )
            /
            max(metadata_a.get("views", 1), 1)
        )
        * 100,
        2
    )

    metadata_a["engagement_rate"] = engagement_a

    # ==========================
    # VIDEO B
    # ==========================
    metadata_b = get_youtube_metadata(
        video_b_url
    )

    transcript_b = get_youtube_transcript(
        video_b_url
    )

    chunks_b = store_video_chunks(
        transcript_b,
        "B"
    )

    engagement_b = round(
        (
            (
                metadata_b.get("likes", 0)
                +
                metadata_b.get("comments", 0)
            )
            /
            max(metadata_b.get("views", 1), 1)
        )
        * 100,
        2
    )

    metadata_b["engagement_rate"] = engagement_b

    return {
        "video_a": {
            "metadata": metadata_a,
            "chunks_saved": chunks_a,
            "transcript_preview": transcript_a[:500]
        },
        "video_b": {
            "metadata": metadata_b,
            "chunks_saved": chunks_b,
            "transcript_preview": transcript_b[:500]
        }
    }


# ==========================
# INSTAGRAM TRANSCRIPT
# ==========================
@router.post("/instagram-transcript")
def instagram_transcript(data: dict):

    transcript = get_instagram_transcript(
        data["instagram_url"]
    )

    return {
        "transcript": transcript[:1000]
    }