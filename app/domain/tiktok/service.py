from . import dto
from fastapi import HTTPException
import logging
from TikTokApi import TikTokApi
import os

class TikTokService:
    def __init__(self, ms_token: str = None) -> None:
        self.ms_token = ms_token
        self.api = TikTokApi()

    async def get_video_download_url(self, body: dto.GetDownloadUrl) -> dict:
        try:
            await self.api.create_sessions(
                ms_tokens=[self.ms_token] if self.ms_token else [os.environ.get("ms_token", None)],
                num_sessions=1,
                sleep_after=3,
                browser=os.getenv("TIKTOK_BROWSER", "chromium")
            )
            video = await self.api.video(url=body.url).info()
            return video.as_dict
        except Exception as e:
            logging.error(f"Error fetching TikTok video: {e}")
            raise HTTPException(status_code=500, detail=f"Error fetching TikTok video: {e}")
        finally:
            await self.api.close_sessions()
