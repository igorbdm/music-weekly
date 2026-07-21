import feedparser

from history import already_sent
from utils import is_last_7_days, parse_date


def contains_any(text, terms):
    normalized_text = text.casefold()
    return any(term.casefold() in normalized_text for term in terms)


def get_video_id(video):
    video_id = video.get("yt_videoid")

    if video_id:
        return video_id

    return video.link.rsplit("=", maxsplit=1)[-1]


def get_feed(channel_name, config):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={config['id']}"

    feed = feedparser.parse(url)

    results = []

    for video in feed.entries:

        if not contains_any(video.title, config["keep"]):
            continue

        if contains_any(video.title, config.get("ignore", [])):
            continue

        if not is_last_7_days(video.published):
            continue

        video_id = get_video_id(video)

        if already_sent(video_id):
            continue

        results.append({
            "channel": channel_name,
            "title": video.title,
            "published": video.published,
            "link": video.link,
            "video_id": video_id,
        })

    return sorted(results, key=lambda video: parse_date(video["published"]), reverse=True)
