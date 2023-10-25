class Tiktok():
    def __init__(self, http: dict) -> None:
        self.http = http
        pass
    def get_video_download_url(self):
        return {"something": self.http}