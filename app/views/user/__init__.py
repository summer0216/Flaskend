from flask import Flask
from app.views.user.user_controller import user


def register_user_views(app: Flask):
    app.register_blueprint(user)
