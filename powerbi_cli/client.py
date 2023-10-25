from functools import cache

import structlog
from azure.identity import DefaultAzureCredential
from pbipy import PowerBI
from requests import Session

SCOPE = "https://analysis.windows.net/powerbi/api/.default"


class PBIClient(PowerBI):
    def __init__(self, bearer_token: str, session: Session = None) -> None:
        super().__init__(bearer_token, session)
        self.logger = structlog.get_logger()


def get_token() -> str:
    """Returns Azure default token"""
    credentials = DefaultAzureCredential()
    access_token = credentials.get_token(SCOPE)
    token = access_token.token
    return token


@cache
def get_client():
    token = get_token()
    return PBIClient(token)
