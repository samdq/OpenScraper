# openscraper/api_integration.py

import requests

class APIIntegration:
    def __init__(self, api_key=None):
        self.api_key = api_key
    def integrate_with_external_api(self, api_url, data):
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            response = requests.post(api_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error integrating with external API {api_url}: {e}")
            return None