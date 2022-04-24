from gateways import github
from collections import defaultdict


def summarize_user_info(user_name):
    all_user_info = github.fetch_user_info(user_name)
    all_user_repos = github.fetch_user_repos(user_name)

    if not all_user_info:
        return None

    summary = {
        'login': all_user_info['login'],
        'name': all_user_info['name'],
        'bio': all_user_info['bio'],
        'languages': defaultdict(lambda: 0),
    }

    if not all_user_repos:
        return summary

    for repo in all_user_repos:
        repo_languages = github.fetch_repo_languages(user_name, repo['name'])

        for language, size_in_bytes in repo_languages.items():
            summary['languages'][language] += size_in_bytes

    return summary


def summarize_repos_info(user_name):
    all_user_repos = github.fetch_user_repos(user_name)

    if not all_user_repos:
        return None

    summary = {}

    for repo in all_user_repos:
        repo_name = repo['name']
        repo_languages = github.fetch_repo_languages(user_name, repo_name)

        summary[repo_name] = repo_languages

    return summary
