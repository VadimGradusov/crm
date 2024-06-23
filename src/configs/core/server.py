"""Server configs"""
import dotenv

FASTAPI_HOST: str = dotenv.get_key('.env', 'FASTAPI_HOST')
FASTAPI_PORT: int = int(dotenv.get_key('.env', 'FASTAPI_PORT'))
