from fastapi import APIRouter
from ..domain.instagram import service, dto

router = APIRouter(
    prefix='/instagram'
)


@router.post("/", status_code=200)
async def get_video_download_url(body: dto.GetDownloadUrl): 
    instagram = service.InstagramService(body.session_id)
    return instagram.get_video_download_url(body)
