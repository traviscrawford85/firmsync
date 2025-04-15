# firm_core/providers/base_provider.py

import time
from abc import ABC, abstractmethod

from utils.token_storage import get_token_path, load_token_data, save_token_data

class BaseProvider(ABC):
    def __init__(self, source: str):
        self.provider_key = source
        self.token_path = get_token_path(source)

        print(f"🔍 [{source.upper()}] Token path resolved → {self.token_path}")

        if not self.token_path:
            raise ValueError(f"❌ Could not resolve token path for: {source}")

        self.token_data = {}

    def load_tokens(self):
        self.token_data = load_token_data(self.provider_key)
        return self.token_data

    def save_tokens(self, tokens):
        save_token_data(tokens, self.provider_key)

    def token_expired(self):
        if not self.token_data:
            return True
        return int(time.time()) >= self.token_data.get("expires_at", 0)

    def refresh_tokens_if_needed(self):
        if self.token_expired():
            print(f"🔁 Refreshing {self.provider_key.upper()} tokens...")
            self.refresh_tokens()
        else:
            print(f"✅ {self.provider_key.upper()} token valid.")

    @abstractmethod
    def refresh_tokens(self):
        pass

    @abstractmethod
    def get_api_client(self):
        pass

    @abstractmethod
    def get_service_layer(self):
        pass
