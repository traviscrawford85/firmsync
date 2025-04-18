# firm_clio/clio_provider.py

import time
import requests
from clio_sdk import Configuration, ApiClient
from firm_core.providers.base_provider import BaseProvider


class ClioProvider(BaseProvider):
    def __init__(self, client_id, client_secret, token_url, api_url):
        super().__init__("clio")
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token_store_path = "clio_tokens_store.json"
        self.api_url = api_url

    def refresh_tokens(self):
        refresh_token = self.token_data["refresh_token"]
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token
        }

        response = requests.post(self.token_url, data=payload)
        if response.status_code != 200:
            raise Exception(f"❌ Failed to refresh Clio token: {response.text}")

        new_tokens = response.json()
        new_tokens["expires_at"] = int(
            time.time()) + new_tokens.get("expires_in", 3600)

        self.save_tokens(new_tokens)
        self.token_data = new_tokens
        print("🔁 Clio tokens refreshed successfully.")

    def get_api_client(self):
        self.load_tokens()
        self.refresh_tokens_if_needed()

        config = Configuration(host=self.api_url)
        config.access_token = self.token_data["access_token"]

        client = ApiClient(config)
        client.default_headers["Authorization"] = f"Bearer {config.access_token}"
        return client

    def get_service_layer(self):
        from custom_services.matter_service import MatterService
        return MatterService()
