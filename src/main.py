from config import settings
from config.logging import logger
from query_parser import get_user_id_and_user_name_from_query
from jira_client import get_jira_issues
from github_client import get_github_activity
from response_generator import format_response_ai, format_response_template


def main():
    """The main chatbot loop."""
    while True:
        query = input("\n👤 ")

        if query.lower() == "exit":
            break

        # 1. Parse the user's question to find a user_id
        user_id, user_name = get_user_id_and_user_name_from_query(query)

        if not user_id or not user_name:
            logger.warning("I'm sorry, I couldn't extract the team member details. Please try again.")
            continue

        # 2. Get the user's account IDs from the mapping
        account_ids = settings.USER_ID_ACCOUNT_IDS.get(user_id)

        if not account_ids:
            logger.warning(f"User {user_name} is not configured in the system. Kindly check the configuration.")
            continue

        logger.info(f"🔍 Looking up recent activity for {user_name.title()}...")

        # 3. Fetch data from APIs
        jira_issues = get_jira_issues(account_ids.get("jira_account_id"))
        github_prs, github_commits = get_github_activity(account_ids.get("github_username"))

        # 4. Generate and print the response
        if settings.USE_AI:
            response_text = format_response_ai(user_name, jira_issues, github_prs, github_commits)
        else:
            response_text = format_response_template(user_name, jira_issues, github_prs, github_commits)

        logger.info(f"🤖 {response_text}")


if __name__ == "__main__":
    logger.info("🤖 JIRA/GitHub Bot Activated. Ask me what a team member is working on.")
    logger.info("   (e.g., 'What is Ram working on?'). Type 'exit' to quit.")

    if settings.USE_AI:
        logger.info("   (OpenAI key found, will generate AI summaries.)")
    else:
        logger.info("   (No OpenAI key, will use template responses.)")

    main()
