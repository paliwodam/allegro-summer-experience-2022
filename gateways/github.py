import os

import requests
from requests.auth import HTTPBasicAuth


def _get_authentication():
    user_name = os.getenv('GITHUB_USER_NAME')
    token = os.getenv('GITHUB_ACCESS_TOKEN')
    if not all([user_name, token]):
        return None

    return HTTPBasicAuth(user_name, token)


def fetch_user_info(username):
    response = requests.get(
        f"https://api.github.com/users/{username}",
        auth=_get_authentication()
    )

    if response.status_code not in range(200, 300):
        print(f"failed to get user info for user: {username} from github, status code {response.status_code}")
        return None
    return response.json()


def fetch_user_repos(username):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        auth=_get_authentication()
    )

    if response.status_code not in range(200, 300):
        print(f"failed to get repos for user: {username} from github, status code {response.status_code}")
        return None
    return response.json()


def fetch_repo_languages(username, repository):
    response = requests.get(
        f"https://api.github.com/repos/{username}/{repository}/languages",
        auth=_get_authentication()
    )

    if response.status_code not in range(200, 300):
        print(f"failed to get repo languages for user: {username} in repo: {repository} from github, status code {response.status_code}")
        return None
    return response.json()

