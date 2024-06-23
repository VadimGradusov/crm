"""Database configs"""
import dotenv

DB_HOST: str = dotenv.get_key('.env', 'DB_HOST')
DB_NAME: str = dotenv.get_key('.env', 'DB_NAME')
DB_USERNAME: str = dotenv.get_key('.env', 'DB_USERNAME')
DB_PASSWORD: str = dotenv.get_key('.env', 'DB_PASSWORD')
