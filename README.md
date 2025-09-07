# Team JIRA Github Activity Chatbot

## Description

This is a command-line AI chatbot that integrates with JIRA and GitHub APIs to answer questions about team member activities. It fetches recent issues, pull requests, and commits for a given user, and generates human-readable summaries using either the OpenAI API or template-based responses.

## Features

- Parse natural language queries to extract team member names
- Fetch assigned JIRA issues and recent updates
- Fetch recent GitHub pull requests and commits
- AI-powered or template-based response generation
- Handles error cases (user not found, no recent activity)
- Simple CLI interface

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone https://github.com/ramsudharsan75/jira-github-chatbot.git
   cd jira-github-chatbot
   ```

2. **Create and activate a Python virtual environment**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   - Copy `.env.example` to `.env` (or edit `.env` directly)
   - Fill in your JIRA and GitHub API credentials:
     ```
     JIRA_BASE_URL="https://your-domain.atlassian.net"
     JIRA_API_USER="your-email@example.com"
     JIRA_API_TOKEN="your-jira-api-token"
     GITHUB_API_TOKEN="your-github-token"
     GITHUB_OWNER="your-github-username"
     ```
   - (Optional) Add your OpenAI API key for AI responses:
     ```
     OPENAI_API_KEY="your-openai-key"
     ```

5. **Configure user mappings**
   - Edit `config/user_data.py` to map user IDs to JIRA and GitHub accounts.

## Usage Instructions

1. **Run the chatbot**

   ```sh
   python src/main.py
   ```

2. **Interact via CLI**

   - Type a question about a team member, e.g.:
     ```
     What is John working on these days?
     Show me recent activity for Sarah
     What has Mike been working on this week?
     ```
   - Type `exit` to quit.

3. **Response Types**
   - If OpenAI API key is set, responses use AI summaries.
   - Otherwise, template-based responses are used.

## Example Queries

- What JIRA tickets is John working on?
- Show me Lisa’s recent pull requests
- What has Mike committed this week?
