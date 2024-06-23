"""Session configs"""
import dotenv

SESSION_ALIVE_HOURS: int = int(dotenv.get_key('.env', 'SESSION_ALIVE_HOURS'))
