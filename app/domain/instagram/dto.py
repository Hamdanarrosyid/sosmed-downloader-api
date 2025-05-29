from pydantic import BaseModel

class GetDownloadUrl(BaseModel):
    url: str
    session_id: str