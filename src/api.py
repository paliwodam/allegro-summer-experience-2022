from flask import Blueprint, jsonify

from src.services import github_info_provider

user_blueprint = Blueprint("simple_page", __name__, url_prefix="/api/user")


@user_blueprint.route("/<user_name>/info", methods=["GET"])
def get_user_info(user_name):
    user_info = github_info_provider.summarize_user_info(user_name)
    return jsonify(user_info)


@user_blueprint.route("/<user_name>/repositories", methods=["GET"])
def get_user_repositories(user_name):
    user_repos = github_info_provider.summarize_repos_info(user_name)
    return jsonify(user_repos)
