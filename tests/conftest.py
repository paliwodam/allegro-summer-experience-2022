import json
import pathlib

import pytest

from src.main import create_app

TEST_DATA_DIRECTORY = pathlib.Path(__file__).parent.joinpath("test_data")


@pytest.fixture
def app():
    return create_app()


def load_json_test_data(file_name):
    with open(f"{TEST_DATA_DIRECTORY}/{file_name}", "r") as f:
        data = json.load(f)
    return data


@pytest.fixture(autouse=True)
def mock_user_info(requests_mock):
    requests_mock.get(
        "https://api.github.com/users/paliwodam",
        json=load_json_test_data("github_user_info.json"),
    )


@pytest.fixture(autouse=True)
def mock_user_repos(requests_mock):
    requests_mock.get(
        "https://api.github.com/users/paliwodam/repos",
        json=load_json_test_data("github_user_repos.json"),
    )


@pytest.fixture(autouse=True)
def mock_languages1(requests_mock):
    requests_mock.get(
        "https://api.github.com/repos/paliwodam/DoublePushOut/languages",
        json=load_json_test_data("github_languages1.json"),
    )


@pytest.fixture(autouse=True)
def mock_languages2(requests_mock):
    requests_mock.get(
        "https://api.github.com/repos/paliwodam/Bomberman/languages",
        json=load_json_test_data("github_languages2.json"),
    )
