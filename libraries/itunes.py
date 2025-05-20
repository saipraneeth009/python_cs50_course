import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

# to print one song from the artist user defines

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# # print(response.json())
# print(json.dumps(response.json(), indent=2))

# to get the trackNames of the artist user defines
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

track_name = response.json()
for result in track_name["results"]:
    print(result["trackName"])