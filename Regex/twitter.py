## using replace and removeprefix

# url = input("URL: ").strip()
# # print(url)

# # username = url.replace("https://twitter.com/","")
# username = url.removeprefix("https://twitter.com/")

# print(f"Username: {username}")

## using re
import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
# print(f"Username: {username}")

## using group (...)
# matches = re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

# if matches := re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(2))

## using non capturing version (?:...)
# if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(1))

if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([\w]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))