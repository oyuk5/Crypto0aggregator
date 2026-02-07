from abc import ABC, abstractmethod
from typing import Optional, Any

import requests
from requests import session


class BaseClient(ABC):
    def __init__(self, base_url: str):
        self.baseUrl = base_url
        self.session = requests.session()

    def _request(self, endpoint: str, params: Optional[dict] = None ) ->Any:
        url = f"{self.baseUrl}{endpoint}"
        try:
            response = self.session.get(url,params=params, timeout = 10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during the request phase to{url}:{e}")
            return None
    @abstractmethod
    def get_price(self, crypto: str) -> float:
        pass