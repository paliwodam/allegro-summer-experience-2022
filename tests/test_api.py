from unittest import mock

import pytest

from src.services import github_info_provider


@pytest.fixture
def mock_summarize_user_info():
    with mock.patch.object(github_info_provider, "summarize_user_info") as mocked_summarize:
        yield mocked_summarize


@pytest.fixture
def mock_summarize_user_repositories():
    with mock.patch.object(github_info_provider, "summarize_repos_info") as mocked_summarize:
        yield mocked_summarize


def test_get_user_info_returns_summarized_info(client, mock_summarize_user_info):
    expected_info = {
        "login": "paliwodam",
        "name": "Martyna Paliwoda",
        "bio": "Student",
        "languages": {"Pascal": 100_000},
    }
    mock_summarize_user_info.return_value = expected_info

    result = client.get("/api/user/paliwodam/info")

    assert result.status_code == 200
    assert result.json == expected_info
    mock_summarize_user_info.assert_called_once_with("paliwodam")


def test_get_user_info_return_404_when_no_user_name_provider(client):
    result = client.get("/api/user//info")

    assert result.status_code == 404


def test_get_user_repositories(client, mock_summarize_user_repositories):
    expected_info = {
        "allegro-summer-experience-2022": {"Python": 12345, "Shell": 500},
        "DifferentialEquations": {"Jupyter Notebook": 9999, "Java": 2137},
    }
    mock_summarize_user_repositories.return_value = expected_info

    result = client.get("/api/user/paliwodam/repositories")

    assert result.status_code == 200
    assert result.json == expected_info


def test_get_user_repositories_return_404_when_no_user_name_provider(client):
    result = client.get("/api/user//repositories")

    assert result.status_code == 404
