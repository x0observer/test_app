import asyncio
import aiohttp
from urllib.parse import urlsplit
import ssl


ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE



async def fetch(session, url, filename):
    async with session.get(url) as response:
        response.raise_for_status()
        content = await response.text()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)


async def fetch_all(url_list, folder):
    tasks = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        for i, url in enumerate(url_list):
            hostname = urlsplit(url).netloc
            filename = f"{folder}/{hostname}{i+1}.html"
            task = asyncio.create_task(fetch(session, url, filename))
            tasks.append(task)
        await asyncio.gather(*tasks)


