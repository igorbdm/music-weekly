from datetime import datetime, timedelta, timezone


def is_last_7_days(date_string):
    published = datetime.fromisoformat(date_string)

    seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)

    return published >= seven_days_ago