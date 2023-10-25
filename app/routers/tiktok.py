from fastapi import APIRouter
from ..domain.tiktok import service, dto
router = APIRouter(prefix='/tiktok')

@router.post("/", status_code=200)
async def get_video_download_url(body: dto.GetDownloadUrl): 
    print(body)
    return service.Tiktok({'http':'dsa'}).get_video_download_url()
