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
    async def scrape_website_async(self, session, url, selector):
        html_content = await self.fetch_html_async(session, url)
        if html_content:
            data = await self.extract_data_async(html_content, selector)
            return data