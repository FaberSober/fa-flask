import os

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
    # Max upload size: 16MB
    MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024)
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-default-secret")
