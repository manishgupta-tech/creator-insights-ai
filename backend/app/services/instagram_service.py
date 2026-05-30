from yt_dlp import YoutubeDL
import os
import whisper


# ==========================
# INSTAGRAM METADATA
# ==========================
def get_instagram_metadata(url: str):

    ydl_opts = {
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )

    return {
        "title": info.get("title"),
        "creator": info.get("uploader"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "views": info.get("view_count"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail")
    }


# ==========================
# DOWNLOAD INSTAGRAM REEL
# ==========================
def download_instagram_video(
    url: str
):

    os.makedirs(
        "downloads",
        exist_ok=True
    )

    output_file = (
        "downloads/instagram_video.mp4"
    )

    ydl_opts = {
        "outtmpl": output_file,
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_file


# ==========================
# TRANSCRIBE VIDEO
# ==========================
def transcribe_instagram_video(
    video_path: str
):

    model = whisper.load_model(
        "base"
    )

    result = model.transcribe(
        video_path
    )

    return result["text"]


# ==========================
# GET INSTAGRAM TRANSCRIPT
# ==========================
def get_instagram_transcript(
    url: str
):

    video_path = (
        download_instagram_video(
            url
        )
    )

    transcript = (
        transcribe_instagram_video(
            video_path
        )
    )

    return transcript