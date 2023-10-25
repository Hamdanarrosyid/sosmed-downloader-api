from fastapi import APIRouter
from ..domain.instagram import service, dto

router = APIRouter(
    prefix='/instagram'
)

instagram = service.InstagramService()

@router.post("/", status_code=200)
async def get_video_download_url(body: dto.GetDownloadUrl): 
    return instagram.get_video_download_url(body)
