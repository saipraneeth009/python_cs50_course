## approach 1 with if statement

# name  = input("name: ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

## using regex

import re

name = input("name: ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     # last, first = matches.groups()
#     # name = f"{first} {last}"
    
#     # last = matches.group(1)
#     # first = matches.group(2)
#     # name = f"{first} {last}"
    
#     name = matches.group(2) + " " + matches.group(1)
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group()
print(f"hello, {name}")