from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.data import Base, engine


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    Base.metadata.create_all(bind=engine)

    @app.get("/")
    async def health_check():
        return {"status": "ok"}

    return app
