import re
from config import settings


def get_user_id_and_user_name_from_query(query) -> tuple[int, str] | tuple[None, None]:
    """Extracts a known user's name from the query."""
    for names, user_id in settings.USERNAMES_USER_ID.items():
        for name in names:
            if re.search(r"\b" + name + r"\b", query, re.IGNORECASE):
                return user_id, name

    return None, None
