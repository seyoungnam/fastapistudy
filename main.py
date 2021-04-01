from fastapi import FastAPI
from loguru import logger
from mylogger import LOG_LEVEL, setup_logging
from uvicorn import Server, Config
from pydantic import BaseModel
from typing import Optional
from config import CONFIG

try:
    PORT = int(CONFIG["PORT"])
except ValueError:
    logger.error(f'PORT env variable should be int: {CONFIG["PORT"]}')


class MyModel(BaseModel):
    name: str
    _id: int
    description: Optional[str] = "Default"


app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("web application started")


@app.get("/app")
async def samplequery(item: str, _id: Optional[int] = 0):
    return {item: _id}


@app.post("/")
async def samplepost(name: str, _id: int, description: Optional[str]):
    return {
        "name": name,
        "id": _id,
        "description": description
    }


if __name__ == '__main__':
    server = Server(
        Config("main:app", host="0.0.0.0", port=PORT, log_level=LOG_LEVEL)
    )

    setup_logging()
    server.run()
