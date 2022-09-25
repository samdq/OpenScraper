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
    def extract_data(self, html, selector):
        try:
            selected_elements = self.selector_engine.select(html, selector)
            return [element.text.strip() for element in selected_elements]
        except Exception as e:
            print(f"Error extracting data with selector '{selector}': {e}")
            return None
    def handle_common_errors(self, response):
        # Handle common HTTP errors and return True if the response is successful
        if response.status_code == 404:
            print("Page not found (404).")
            return False
        elif response.status_code == 403:
            print("Access forbidden (403).")
            return False
        elif response.status_code == 500:
            print("Internal server error (500).")
            return False
        return True