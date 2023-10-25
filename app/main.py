from fastapi import FastAPI, HTTPException
from .routers import instagram, tiktok
from starlette.requests import Request
from starlette.responses import JSONResponse


app = FastAPI()

@app.exception_handler(HTTPException)
async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": exc.detail}, status_code=exc.status_code)


app.include_router(instagram.router, prefix='/api')
app.include_router(tiktok.router, prefix='/api')

@app.get('/')
async def root():
    return {"message": "sosmed-downloader-api", "version": "v.0.1"}