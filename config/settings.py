from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JIRA_API_TOKEN: str
    JIRA_BASE_URL: str
    JIRA_API_USER: str
    GITHUB_API_TOKEN: str
    GITHUB_OWNER: str
    OPENAI_API_KEY: str = ""
    USERNAMES_USER_ID: dict[tuple, int] = {
        ("ramsudharsan75", "ram", "ramsudharsan"): 1
    }
    USER_ID_ACCOUNT_IDS: dict[int, dict[str, str]] = {
        1: {
            "jira_account_id": "5a02e9030793706225b9aecb",
            "github_username": "ramsudharsan75",
        },
    }
    USE_AI: bool = False

    def model_post_init(self, _):
        self.USE_AI = bool(self.OPENAI_API_KEY)

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
