import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    APP_NAME = "Open Source Pirate"
    DEBUG = True
    TESTING = False
    # SECRET_KEY

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 3001))

config = BaseConfig()
