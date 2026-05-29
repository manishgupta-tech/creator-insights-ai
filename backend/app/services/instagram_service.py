from yt_dlp import YoutubeDL


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