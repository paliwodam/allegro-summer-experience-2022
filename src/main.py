from flask import Flask

from src.api import user_blueprint

app = Flask(import_name=__name__)
app.register_blueprint(user_blueprint)
