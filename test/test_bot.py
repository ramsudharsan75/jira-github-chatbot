from src.query_parser import get_user_id_and_user_name_from_query
from src.response_generator import format_response_template
from unittest.mock import patch


def test_query_parser_valid_user():
    user_names_user_id = {
        ("ram", "ramsudharsan75", "ramsudharsan"): 1,
    }
    user_id, user_name = get_user_id_and_user_name_from_query("What is Ram working on these days?", user_names_user_id)
    assert user_id is not None and user_name is not None
    assert user_name == "ram"


def test_query_parser_invalid_user():
    user_names_user_id = {}
    user_id, user_name = get_user_id_and_user_name_from_query("What is UnknownUser working on?", user_names_user_id)
    assert user_id is None or user_name is None


def test_jira_issues_found():
    with patch("src.jira_client.get_jira_issues", return_value=["JIRA-123", "JIRA-456"]) as mock_jira:
        issues = mock_jira(1)
        assert isinstance(issues, list)
        assert issues == ["JIRA-123", "JIRA-456"]
        mock_jira.assert_called_once_with(1)


def test_github_activity_found():
    with patch("src.github_client.get_github_activity", return_value=(["PR #1"], ["Commit abc"])) as mock_github:
        prs, commits = mock_github(1)
        assert isinstance(prs, list)
        assert isinstance(commits, list)
        assert prs == ["PR #1"]
        assert commits == ["Commit abc"]
        mock_github.assert_called_once_with(1)


def test_response_no_activity():
    response = format_response_template("NoActivityUser", [], [], [])
    assert "couldn't find any recent activity" in response


def test_response_with_activity():
    response = format_response_template("John", ["JIRA-123"], ["PR #1"], ["Commit abc"])
    assert "Here's what John seems to be working on:" in response
    assert "**Current JIRA Tickets:**" in response
    assert "**Recent GitHub Pull Requests:**" in response
    assert "**Recent GitHub Commits:**" in response
