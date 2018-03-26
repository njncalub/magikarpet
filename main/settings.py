import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


DATABASE_URL = os.getenv('DATABASE_URL', "mongodb://localhost:27017")
DATABASE_NAME = os.getenv('DATABASE_NAME', "magikarpet")
