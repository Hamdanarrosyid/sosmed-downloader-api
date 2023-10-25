from . import dto
import requests
from .utils import headers
import re
from fastapi import HTTPException
import logging

class InstagramService():
    def __init__(self) -> None:
        self.baseURL = 'https://www.instagram.com/api/graphql'
        pass

    def get_video_download_url(self, body: dto.GetDownloadUrl) -> dto.GetDownloadUrl:
        short_code = self.get_short_code(body.url)
        headers['referer'] = f'https://www.instagram.com/p/{short_code}/'
        raw_data = f'av=0&__d=www&__user=0&__a=1&__req=3&__hs=19655.HYP%3Ainstagram_web_pkg.2.1..0.0&dpr=1&__ccg=UNKNOWN&__rev=1009466525&__s=otsihg%3A4upelk%3Av7cj17&__hsi=7293830036142173767&__dyn=7xeUmwlEnwn8K2WnFw9-2i5U4e1ZyUW3qi2K360CEbo1nEhw2nVE4W0om78b87C0yE5ufz81s8hwGwQwoEcE7O2l0Fwqo31w9a9x-0z8-U2zxe2GewGwso88cobEaU2eUlwhEe87q7-0iK2S3qazo7u1xwIw8O321LwTwKG1pg661pwr86C1mwraCgoK68&__csr=gtsG9HmhuGvQJ2vah4VAAXBVrAZ9BBgBrWZqVEhAhWyrV4US8n-AiVXGviHAUObKELopiAj8Aal4Gvhe8WGGwODKew04ni80VQ0gq0gq08YzA4oS02kWeUh6aexq9w8Ca9ofFE1by02z60aYw3lj09O0rN00ppE0gMw&__comet_req=7&lsd=AVpKq9If6G0&jazoest=2856&__spin_r=1009466525&__spin_b=trunk&__spin_t=1698227142&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisPostActionLoadPostQueryQuery&variables=%7B%22shortcode%22%3A%22{short_code}%22%2C%22fetch_comment_count%22%3A40%2C%22fetch_related_profile_media_count%22%3A3%2C%22parent_comment_count%22%3A24%2C%22child_comment_count%22%3A3%2C%22fetch_like_count%22%3A10%2C%22fetch_tagged_user_count%22%3Anull%2C%22fetch_preview_comment_count%22%3A2%2C%22has_threaded_comments%22%3Atrue%2C%22hoisted_comment_id%22%3Anull%2C%22hoisted_reply_id%22%3Anull%7D&server_timestamps=true&doc_id=10015901848480474'
        resp = requests.post(self.baseURL, data=raw_data, headers=headers)
        response_dict = resp.json()
        return {'url': response_dict['data']['xdt_shortcode_media']['video_url']}
    
    def get_short_code(self, url: str) -> str:
        if url[-1] == '/':
            url = url[:-1]
        code_pattern = r'/([^/]+)$'
        try:  
            code = re.findall(code_pattern, url)[0]
        except Exception as e:
            error_data = {'url': url, 'error': e}
            logging.error(msg=f'failed get short code {error_data}')
            raise HTTPException(status_code=500, detail=f'failed get short code from url')
            
        return code

