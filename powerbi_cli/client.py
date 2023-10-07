import typing as t
from functools import cached_property
from urllib.parse import urljoin

import requests
from azure.identity import DefaultAzureCredential

SCOPE = "https://analysis.windows.net/powerbi/api/.default"


class PowerBIClient:
    base_url = "https://api.powerbi.com/v1.0/myorg/"

    @cached_property
    def token(self):
        credentials = DefaultAzureCredential()
        access_token = credentials.get_token(SCOPE)
        token = access_token.token
        return token

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get(self, endpoint, params: t.Optional[dict] = None):
        url = urljoin(self.base_url, endpoint)
        res = requests.get(url, params=params, headers=self.headers, timeout=60)
        return res


client = PowerBIClient()
