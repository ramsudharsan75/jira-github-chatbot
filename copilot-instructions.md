# AI Agent Assignment: Team Activity Monitor (2-Day Sprint)
## Project Overview

Build a simple AI chatbot that integrates with JIRA and GitHub APIs to answer basic
questions about team member activities. This is a rapid prototyping exercise to demonstrate
API integration and problem-solving skills.

## Objective

Create a working prototype that can answer the question: **“What is [member] working on
these days?”** by fetching data from JIRA and GitHub.

## Core Requirements

### 1. Simple Chat Interface

Basic web interface with input/output (can be simple HTML + JavaScript)
OR command-line interface
Accept natural language questions about team members

### 2. JIRA Integration

**Required endpoints:**
Get assigned issues for a user
Fetch issue status and recent updates
Basic authentication (API token)
**Example queries to handle:**
“What JIRA tickets is John working on?”
“Show me Sarah’s current issues”

### 3. GitHub Integration

**Required endpoints:**
Get recent commits by user
Fetch active pull requests
List repositories user contributed to recently
**Example queries to handle:**
“What has Mike committed this week?”
“Show me Lisa’s recent pull requests”

### 4. AI Response Generation

Use OpenAI API, Claude API, or simple template-based responses
Combine JIRA and GitHub data into human-readable answers
Handle basic error cases (user not found, no recent activity)

## Technical Requirements

### Minimal Tech Stack

**Backend**: Node.js/Python (Express/Flask)
**Frontend**: Simple HTML/CSS/JS or CLI
**AI**: OpenAI API (GPT-3.5) or template responses
**APIs**: JIRA REST API + GitHub REST API

### Must-Have Features

● **Authentication**: Basic API token auth for JIRA and GitHub
● **User Query Processing**: Parse user questions to extract member names
● **Data Fetching**: Get recent activity from both platforms
● **Response Formatting**: Present data in conversational format

## Implementation Tasks

### Core Development Tasks

[ ] Project setup and environment configuration
[ ] JIRA API authentication and basic connection
[ ] Implement endpoint to fetch user’s assigned issues
[ ] GitHub API authentication and basic connection
[ ] Implement endpoint to fetch user’s recent commits and PRs
[ ] Create simple data processing functions
[ ] Test both API integrations independently
[ ] Implement basic query parsing (extract user names from questions)
[ ] Integrate AI API for response generation OR create response templates
[ ] Combine JIRA and GitHub data into coherent answers
[ ] Handle basic error scenarios
[ ] Build simple user interface (web or CLI)
[ ] End-to-end testing with real data
[ ] Documentation and demo preparation
[ ] Code cleanup and final testing

## Deliverables

### Required (End of Day 2):

● **Working Application**: Functional chatbot that answers the core question
● **Source Code**: Clean, commented code with clear structure
● **Demo**: 10-minute demonstration of the working system
● **Basic Documentation**: Setup instructions and API usage

### Test Cases to Implement:

“What is John working on these days?”
“Show me recent activity for Sarah”
“What has Mike been working on this week?”
Handle case when user has no recent activity
Handle case when user is not found
