from flask import Flask
from flask_restx import Api
from .config import Config
from .api.image import api as image_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app, title="Image Recognition API", version="1.0", description="Simple REST API for image recognition")
    api.add_namespace(image_ns, path="/api/image")

    return app
