from flask import Flask

from src.api import user_blueprint


def create_app():
    app = Flask(import_name=__name__)
    app.register_blueprint(user_blueprint)
    return app


app = create_app()
