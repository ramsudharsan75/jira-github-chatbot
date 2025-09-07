import json

import openai
from config import settings, logger


def format_response_template(name, jira_issues, github_prs, github_commits):
    """Generates a human-readable response using simple templates."""
    if not jira_issues and not github_prs and not github_commits:
        return f"I couldn't find any recent activity for {name.title()}."

    response_parts = [f"Here's what {name.title()} seems to be working on:"]

    if jira_issues:
        response_parts.append("\n**Current JIRA Tickets:**")
        response_parts.extend(jira_issues)

    if github_prs:
        response_parts.append("\n**Recent GitHub Pull Requests:**")
        response_parts.extend(github_prs)

    if github_commits:
        response_parts.append("\n**Recent GitHub Commits:**")
        response_parts.extend(github_commits)

    return "\n".join(response_parts)


def format_response_ai(name, jira_issues, github_prs, github_commits):
    """Generates a summary using the OpenAI API."""
    if not settings.OPENAI_API_KEY:
        return "OpenAI API key not configured. Falling back to template."

    if not jira_issues and not github_prs and not github_commits:
        return f"I couldn't find any recent activity for {name.title()}."

    # Create a structured prompt for the AI
    prompt = f"""
    Summarize the recent work of a team member named {name.title()} in a brief, conversational paragraph. 
    Use the following raw data from JIRA and GitHub. If a category is empty, don't mention it.

    JIRA Tickets:
    {json.dumps(jira_issues, indent=2)}

    GitHub Pull Requests:
    {json.dumps(github_prs, indent=2)}
    
    GitHub Commits:
    {json.dumps(github_commits, indent=2)}
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant summarizing a team member's work.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        response_content = response.choices[0].message.content
        return response_content.strip() if response_content else ""
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {e}")
        return (
            "There was an issue generating an AI summary. Here is the raw data instead."
        )
