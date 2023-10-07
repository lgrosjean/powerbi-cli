import os

from azure.identity import DefaultAzureCredential
from pbipy import PowerBI

SCOPE = "https://analysis.windows.net/powerbi/api/.default"


def get_token() -> str:
    """Returns Azure default token"""
    credentials = DefaultAzureCredential()
    access_token = credentials.get_token(SCOPE)
    token = access_token.token
    return token


OFFLINE = os.getenv("OFFLINE", "False")

if OFFLINE != "True":
    _TOKEN = get_token()

    pbi: PowerBI = PowerBI(_TOKEN)
