import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import collector
import history
from utils import is_last_7_days


class CollectorTests(unittest.TestCase):
    def test_contains_any_is_case_insensitive(self):
        self.assertTrue(collector.contains_any("A FULL performance", ["full performance"]))
        self.assertFalse(collector.contains_any("A concert", ["full performance"]))

    def test_get_video_id_uses_feed_value(self):
        self.assertEqual(
            collector.get_video_id({"yt_videoid": "abc123", "link": "https://youtube.com/watch?v=ignored"}),
            "abc123",
        )


class HistoryTests(unittest.TestCase):
    def test_marks_multiple_videos_without_duplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary_file = Path(directory) / "sent_videos.json"

            with patch.object(history, "HISTORY_FILE", temporary_file):
                history.mark_as_sent(["one", "two", "one"])
                self.assertTrue(history.already_sent("one"))
                self.assertTrue(history.already_sent("two"))
                self.assertFalse(history.already_sent("three"))


class DateTests(unittest.TestCase):
    def test_accepts_recent_and_rejects_old_dates(self):
        recent = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        old = (datetime.now(timezone.utc) - timedelta(days=8)).isoformat()

        self.assertTrue(is_last_7_days(recent))
        self.assertFalse(is_last_7_days(old))


if __name__ == "__main__":
    unittest.main()
