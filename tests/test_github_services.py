from src.services import github_info_provider


def test_summarize_user_info():
    result = github_info_provider.summarize_user_info("paliwodam")

    assert result["login"] == "paliwodam"
    assert result["name"] == "Martyna Paliwoda"
    assert result["bio"] == "Student of Computer Science at AGH University of Science and Technology"
    assert result["languages"]["Python"] == 10384
    assert result["languages"]["Java"] == 65936
    assert result["languages"]["JavaScript"] == 602
    assert result["languages"]["HTML"] == 581
    assert "CSS" not in result.keys()
    assert "Jupyter Notebook" not in result.keys()


def test_get_user_repos():
    result = github_info_provider.summarize_repos_info("paliwodam")

    assert result["Bomberman"] == {"Java": 65936, "JavaScript": 602, "HTML": 581}
    assert result["DoublePushout"] == {"Python": 10384}
