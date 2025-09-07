from datetime import datetime, timedelta

import requests
from config import settings, logger
from response_generator import parse_pr_response, parse_commit_response


def get_github_activity(github_username) -> tuple[list[str], list[str]]:
    """Fetches recent commits and pull requests for a GitHub user."""
    activity_start_datetime = (datetime.now() - timedelta(days=settings.GITHUB_RECENT_ACTIVITY_DAYS)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    prs = _get_github_prs(activity_start_datetime, github_username)
    commits = _get_github_commits(activity_start_datetime, github_username)
    return prs, commits


def _get_github_prs(activity_start_datetime: str, github_username: str) -> list[str]:
    """Fetches recent pull requests for a GitHub user."""
    pr_search_query = f"q=is:pr+author:{github_username}+created:>{activity_start_datetime}"
    url_prs = f"{settings.GITHUB_SEARCH_BASE_URL}/issues?{pr_search_query}"

    try:
        response_prs = requests.get(url_prs, headers=settings.GITHUB_HEADERS)
        response_prs.raise_for_status()
        pr_items = response_prs.json().get("items", [])
        return parse_pr_response(pr_items)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching GitHub PRs: {e}")

    return []


def _get_github_commits(activity_start_datetime: str, github_username: str) -> list[str]:
    """Fetches recent commits for a GitHub user."""
    commit_search_query = f"q=committer:{github_username}+committer-date:>{activity_start_datetime}"
    url_commits = f"{settings.GITHUB_SEARCH_BASE_URL}/commits?{commit_search_query}"
    headers_commits = settings.GITHUB_HEADERS.copy()
    headers_commits.update(settings.GITHUB_SEARCH_COMMIT_ACCEPT_HEADER)

    try:
        response_commits = requests.get(url_commits, headers=headers_commits)
        response_commits.raise_for_status()
        commit_items = response_commits.json().get("items", [])
        return parse_commit_response(commit_items)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching GitHub commits: {e}")

    return []
