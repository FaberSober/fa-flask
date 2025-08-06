from flask import Flask
from flask_restx import Api
from prometheus_flask_exporter import PrometheusMetrics
from .config import Config
from .api.image import api as image_ns
from .api.api import api as demo_api_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化 prometheus exporter，监控指标暴露
    metrics = PrometheusMetrics(app)
    # static information as metric
    metrics.info('app_info', 'Application info', version='1.0.0')

    # 注册 Flask-RESTX API
    api = Api(app, title="Image Recognition API", version="1.0", description="Simple REST API for image recognition", doc='/docs')

    api.add_namespace(image_ns, path="/api/image")
    api.add_namespace(demo_api_ns, path="/api/demo")

    return app
