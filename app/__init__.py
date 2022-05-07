import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.configs import config

db = SQLAlchemy()


def create_app(config_name=None):
    app = Flask(os.path.abspath((os.path.join(os.path.dirname(__file__), ".."))))
    if not config_name:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    # 引入数据库配置
    app.config.from_object(config[config_name])
    db.init_app(app)

    from app.views import init_view
    # 注册路由
    init_view(app)

    return app
