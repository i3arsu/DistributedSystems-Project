from fastapi import FastAPI

from routes.crypt import router as main_router

app = FastAPI()

app.include_router(main_router)