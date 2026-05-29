from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url: str):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    return None


def get_youtube_metadata(url: str):

    ydl_opts = {
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "creator": info.get("uploader"),
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "duration": info.get("duration"),
        "upload_date": info.get("upload_date"),
        "video_id": info.get("id")
    }




def get_youtube_transcript(url: str):

    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    full_text = " ".join(
        chunk.text
        for chunk in transcript
    )

    return full_text