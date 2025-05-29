from pydantic import BaseModel
from typing import Optional

class GetDownloadUrl(BaseModel):
    url: str
    ms_token: Optional[str] = None
