# openscraper/asynchronous_scraping.py

import aiohttp
import asyncio

class AsynchronousScraper:
    def __init__(self, max_concurrent_requests=5):
        self.max_concurrent_requests = max_concurrent_requests

    async def fetch_html_async(self, session, url):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"Error fetching HTML from {url}: {e}")
            return None
