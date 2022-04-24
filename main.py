import os.path

from flask import Flask, jsonify
from dotenv import load_dotenv
from service import github_info_provider

if os.path.isfile(".env"):
    load_dotenv(".env")

app = Flask(import_name=__name__)


@app.route("/api/user/<user_name>/info", methods=["GET"])
def get_user_info(user_name):
    user_info = github_info_provider.summarize_user_info(user_name)
    return jsonify(user_info)


@app.route("/api/user/<user_name>/repositories", methods=["GET"])
def get_user_repositories(user_name):
    user_repos = github_info_provider.summarize_repos_info(user_name)
    return jsonify(user_repos)


if __name__ == "__main__":
    app.run(debug=True)
