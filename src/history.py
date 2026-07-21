import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
HISTORY_FILE = PROJECT_ROOT / "data" / "sent_videos.json"


def load_history():
    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history):
    HISTORY_FILE.parent.mkdir(exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def already_sent(video_id):
    history = load_history()
    return video_id in history


def mark_as_sent(video_ids):
    """Registra os vídeos somente depois de o e-mail ter sido enviado."""
    history = load_history()

    for video_id in video_ids:
        if video_id not in history:
            history.append(video_id)

    save_history(history)
