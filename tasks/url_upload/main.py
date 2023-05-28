import asyncio 
from fetcher import fetch_all
from file_reader import read_urls_from_file

if __name__ == "__main__":
    urls = read_urls_from_file()
    folder_path = "uploads"
    asyncio.run(fetch_all(urls, folder_path))