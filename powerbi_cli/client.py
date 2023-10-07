import os
from functools import cache

from azure.identity import DefaultAzureCredential
from pbipy import PowerBI

SCOPE = "https://analysis.windows.net/powerbi/api/.default"


def get_token() -> str:
    """Returns Azure default token"""
    credentials = DefaultAzureCredential()
    access_token = credentials.get_token(SCOPE)
    token = access_token.token
    return token


@cache
def get_client():
    token = get_token()
    return PowerBI(token)
