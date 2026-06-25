import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

if env_path.exists():
    load_dotenv(env_path)

class Config:
    USERNAME = os.getenv("ORANGE_USERNAME")
    PASSWORD = os.getenv("ORANGE_PASSWORD")