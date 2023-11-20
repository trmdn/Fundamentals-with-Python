import re

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"

link_search = input()

while link_search:
    matches = re.search(pattern, link_search)
    if matches:
        valid_url = matches.group(1)
        print(valid_url)
    link_search = input()