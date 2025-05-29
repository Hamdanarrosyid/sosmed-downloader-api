from fastapi import APIRouter
from ..domain.tiktok import service, dto

router = APIRouter(
    prefix='/tiktok'
)

@router.post("/", status_code=200)
async def get_video_download_url(body: dto.GetDownloadUrl):
    tiktok = service.TikTokService(body.ms_token)
    return await tiktok.get_video_download_url(body)
