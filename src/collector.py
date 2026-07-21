import feedparser

from history import already_sent
from utils import is_last_7_days


def get_feed(channel_name, config):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={config['id']}"

    feed = feedparser.parse(url)

    results = []

    for video in feed.entries:

        if not any(text in video.title for text in config["keep"]):
            continue

        if not is_last_7_days(video.published):
            continue

        if already_sent(video.link):
            continue

        results.append({
            "channel": channel_name,
            "title": video.title,
            "published": video.published,
            "link": video.link,
        })

    return results