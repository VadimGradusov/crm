"""Init"""
import uvicorn
from src.app.core.fastapi.app import app
from src.configs.core.server import FASTAPI_HOST, FASTAPI_PORT
from src.app.common import api
from src import configs


if __name__ == '__main__':
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
