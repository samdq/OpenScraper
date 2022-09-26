# openscraper/selector_engine.py

from bs4 import BeautifulSoup

class SelectorEngine:
    def select(self, html, selector):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            selected_elements = soup.select(selector)
            return selected_elements
        except Exception as e:
            print(f"Error selecting elements with selector '{selector}': {e}")
            return None
