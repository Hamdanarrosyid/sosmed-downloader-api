from pydantic import BaseModel

class GetDownloadUrl(BaseModel):
    url: str