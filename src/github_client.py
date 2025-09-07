from datetime import datetime, timedelta

import requests
from config import settings, logger

GITHUB_HEADERS = {"Authorization": f"token {settings.GITHUB_API_TOKEN}"}


def get_github_activity(github_username):
    """Fetches recent commits and pull requests for a GitHub user."""
    if not github_username:
        return None, None

    # Calculate date for "this week"
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get recent pull requests
    prs = []
    
    try:
        url_prs = f"https://api.github.com/search/issues?q=is:pr+author:{github_username}+created:>{one_week_ago}"
        response_prs = requests.get(url_prs, headers=GITHUB_HEADERS)
        response_prs.raise_for_status()
        pr_items = response_prs.json().get("items", [])
        prs = [f"- PR #{pr['number']}: {pr['title']} in {pr['repository_url'].split('/')[-1]}" for pr in pr_items[:5]]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching GitHub PRs: {e}")

    # Get recent commits
    commits = []
    try:
        url_commits = f"https://api.github.com/search/commits?q=author:{github_username}+committer-date:>{one_week_ago}"
        headers_commits = GITHUB_HEADERS.copy()
        headers_commits["Accept"] = "application/vnd.github.cloak-preview"  # Required for this search endpoint
        response_commits = requests.get(url_commits, headers=headers_commits)
        response_commits.raise_for_status()
        commit_items = response_commits.json().get("items", [])
        commits = [
            f"- Commit in {commit['repository']['name']}: {commit['commit']['message'].splitlines()[0]}"
            for commit in commit_items[:5]
        ]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching GitHub commits: {e}")

    return prs, commits
