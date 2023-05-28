def read_urls_from_file(file_path: str = "urls.txt"):
    urls = []
    with open(file_path, "r") as file:
        for line in file:
            url = line.strip()
            if url:
                urls.append(url)
    return urls


urls = read_urls_from_file()
print(urls)