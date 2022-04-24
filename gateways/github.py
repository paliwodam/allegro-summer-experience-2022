import requests


def fetch_user_info(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code not in range(200, 300):
        print(f"failed to get user info for user: {username} from github, status code {response.status_code}")
        return None
    return response.json()


def fetch_user_repos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    if response.status_code not in range(200, 300):
        print(f"failed to get repos for user: {username} from github, status code {response.status_code}")
        return None
    return response.json()


def fetch_repo_languages(username, repository):
    response = requests.get(f"https://api.github.com/repos/{username}/{repository}/languages")
    if response.status_code not in range(200, 300):
        print(f"failed to get repo languages for user: {username} in repo: {repository} from github, status code {response.status_code}")
        return None
    return response.json()

