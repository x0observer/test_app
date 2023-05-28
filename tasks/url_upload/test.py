import unittest
import os
import shutil
import asyncio
import aiohttp
from urllib.parse import urlsplit
from main import fetch_all


class FetchAllTestCase(unittest.TestCase):
    def setUp(self):
        self.urls = [
            "https://www.google.com",
            "https://www.python.org"
        ]
        self.folder_path = "test_pages"

    def tearDown(self):
        shutil.rmtree(self.folder_path)

    def test_fetch_all(self):
        asyncio.run(fetch_all(self.urls, self.folder_path))

        # Check the existence of saved files
        self.assertTrue(os.path.exists(self.folder_path))
        self.assertEqual(len(os.listdir(self.folder_path)), len(self.urls))

        # Check the content of saved files
        for i, url in enumerate(self.urls):
            hostname = urlsplit(url).netloc
            filename = f"{self.folder_path}/{hostname}{i+1}.html"
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                self.assertTrue(content.startswith("<!doctype html"))
                self.assertIn(url, content)

unittest.main()