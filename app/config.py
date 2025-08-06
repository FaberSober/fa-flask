import os

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-default-secret")
    # Max upload size: 16MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
