from pydantic import BaseModel
from typing import Type

class ServiceProvider(BaseModel):
    username: str | None = None
    get_video_url: function()
