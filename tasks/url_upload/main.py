import asyncio 
from fetcher import fetch_all
from file_reader import read_urls_from_file


FOLDER_PATH = "uploads"

if __name__ == "__main__":
    urls = read_urls_from_file()
    asyncio.run(fetch_all(urls, FOLDER_PATH))