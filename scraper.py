# openscraper/scraper.py

import requests
from openscraper.selector_engine import SelectorEngine

class Scraper:
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.selector_engine = SelectorEngine()

    def fetch_html(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching HTML from {url}: {e}")
            return None