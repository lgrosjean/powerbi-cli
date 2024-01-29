from functools import cache

import structlog
from azure.identity import DefaultAzureCredential
from pbipy import PowerBI

SCOPE = "https://analysis.windows.net/powerbi/api/.default"


class PBIClient(PowerBI):
    def __init__(self, bearer_token: str) -> None:
        super().__init__(bearer_token)
        self.logger = structlog.get_logger(self.__class__.__name__)


def get_token() -> str:
    """Returns Azure default token. The following credential types if
    enabled will be tried, in order:
    - EnvironmentCredential
    - VisualStudioCodeCredential
    - AzureCliCredential
    - InteractiveBrowserCredential
    """
    credentials = DefaultAzureCredential()
    access_token = credentials.get_token(SCOPE)
    token = access_token.token
    return token


@cache
def get_client():
    token = get_token()
    return PBIClient(token)
