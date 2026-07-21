import json
from pathlib import Path


HISTORY_FILE = Path("data/sent_videos.json")


def load_history():
    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history):
    HISTORY_FILE.parent.mkdir(exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def already_sent(link):
    history = load_history()
    return link in history


def mark_as_sent(link):
    history = load_history()

    if link not in history:
        history.append(link)
        save_history(history)