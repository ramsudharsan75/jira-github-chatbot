import requests
from requests.auth import HTTPBasicAuth

from config import settings, logger

JIRA_AUTH = HTTPBasicAuth(settings.JIRA_API_USER, settings.JIRA_API_TOKEN)


def get_jira_issues(jira_account_id):
    """Fetches assigned and in-progress JIRA issues for a user."""
    if not jira_account_id:
        return None

    url = f"{settings.JIRA_BASE_URL}/rest/api/3/search"
    headers = {"Accept": "application/json"}
    # JQL to find issues assigned to the user that are not done or closed
    jql = f'assignee = "{jira_account_id}" AND status not in (Done, Closed, "To Do") ORDER BY updated DESC'
    query = {"jql": jql, "fields": "summary,status,updated"}

    try:
        response = requests.get(url, headers=headers, params=query, auth=JIRA_AUTH)
        response.raise_for_status()
        issues = response.json().get("issues", [])
        return [
            f"- {issue['key']}: {issue['fields']['summary']} (Status: {issue['fields']['status']['name']})"
            for issue in issues[:5]
        ]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching JIRA issues: {e}")
        return []
