from src.gateways import github


def test_fetch_user_info():
    result = github.fetch_user_info("paliwodam")

    assert result["login"] == "paliwodam"
    assert result["name"] == "Martyna Paliwoda"
    assert result["bio"] == "Student of Computer Science at AGH University of Science and Technology"


def test_fetch_user_repos():
    result = github.fetch_user_repos("paliwodam")

    assert len(result) == 2
    assert result[0]["name"] == "Bomberman"
    assert result[1]["name"] == "DoublePushout"


def test_fetch_repo_languages():
    result = github.fetch_repo_languages("paliwodam", "DoublePushout")

    assert result == {"Python": 10384}
    assert "Java" not in result.keys()

    result = github.fetch_repo_languages("paliwodam", "Bomberman")

    assert result["Java"] == 65936
    assert result["JavaScript"] == 602
    assert result["HTML"] == 581
    assert "Python" not in result.keys()
