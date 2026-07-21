from urllib.request import urlopen

url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC3I2GFN_F8WudD_2jUZbojA"

with urlopen(url) as response:
    print(response.status)
    print(response.read(300).decode("utf-8"))