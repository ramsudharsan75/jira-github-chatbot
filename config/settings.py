from pydantic_settings import BaseSettings, SettingsConfigDict

from config import user_data


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    JIRA_API_TOKEN: str
    JIRA_BASE_URL: str
    JIRA_API_USER: str
    GITHUB_SEARCH_BASE_URL: str
    GITHUB_API_TOKEN: str
    GITHUB_OWNER: str
    OPENAI_API_KEY: str = ""
    GITHUB_RECENT_ACTIVITY_DAYS: int = 7
    GITHUB_HEADERS: dict[str, str] = {}
    GITHUB_SEARCH_COMMIT_ACCEPT_HEADER: dict[str, str]

    USERNAMES_USER_ID: dict[tuple, int] = user_data.USERNAMES_USER_ID
    USER_ID_ACCOUNT_IDS: dict[int, dict[str, str]] = user_data.USER_ID_ACCOUNT_IDS

    USE_AI: bool = False

    def model_post_init(self, _):
        self.USE_AI = bool(self.OPENAI_API_KEY)
        self.GITHUB_HEADERS = {"Authorization": f"token {self.GITHUB_API_TOKEN}"}


settings = Settings()  # type: ignore
