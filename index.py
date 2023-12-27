from fastapi import FastAPI

from routes.crypt import router as crypt_router

app = FastAPI()

app.include_router(crypt_router)