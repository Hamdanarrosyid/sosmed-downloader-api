from . import dto
from fastapi import HTTPException
import logging
from instagrapi import Client

class InstagramService():
    def __init__(self, session_id: str) -> None:
        self.cl = Client()
        self.cl.login_by_sessionid(session_id)

    def get_video_download_url(self, body: dto.GetDownloadUrl) -> dict:
        media_pk = self.cl.media_pk_from_url(body.url)
        if not media_pk:
            logging.error(f"Invalid URL: {body.url}")
            raise HTTPException(status_code=400, detail="Invalid URL")
        media = self.cl.media_info(media_pk).model_dump()
        return media
