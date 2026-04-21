"""
Time and date manipulation utilities.
"""

from datetime import datetime, timedelta
from typing import Optional, List
import time


def now() -> datetime:
    """Get the current datetime."""
    return datetime.now()


def now_timestamp() -> float:
    """Get the current Unix timestamp."""
    return time.time()


def datetime_to_timestamp(dt: datetime) -> float:
    """Convert a datetime to Unix timestamp."""
    return dt.timestamp()


def timestamp_to_datetime(timestamp: float) -> datetime:
    """Convert a Unix timestamp to datetime."""
    return datetime.fromtimestamp(timestamp)


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime as a string."""
    return dt.strftime(format_str)


def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Parse a datetime string into a datetime object."""
    return datetime.strptime(date_str, format_str)


def add_days(dt: datetime, days: int) -> datetime:
    """Add days to a datetime."""
    return dt + timedelta(days=days)


def add_hours(dt: datetime, hours: int) -> datetime:
    """Add hours to a datetime."""
    return dt + timedelta(hours=hours)


def add_minutes(dt: datetime, minutes: int) -> datetime:
    """Add minutes to a datetime."""
    return dt + timedelta(minutes=minutes)


def time_ago(dt: datetime) -> str:
    """Get a human-readable time ago string."""
    now_dt = now()
    diff = now_dt - dt
    
    seconds = int(diff.total_seconds())
    
    if seconds < 60:
        return f"{seconds} seconds ago"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    hours = minutes // 60
    if hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    days = hours // 24
    if days < 30:
        return f"{days} day{'s' if days != 1 else ''} ago"
    months = days // 30
    if months < 12:
        return f"{months} month{'s' if months != 1 else ''} ago"
    years = months // 12
    return f"{years} year{'s' if years != 1 else ''} ago"


def get_date_range(start_date: datetime, end_date: datetime) -> List[datetime]:
    """Get a list of datetimes for each day in a date range."""
    date_list = []
    current = start_date
    while current <= end_date:
        date_list.append(current)
        current += timedelta(days=1)
    return date_list


def is_weekend(dt: datetime) -> bool:
    """Check if a datetime falls on a weekend."""
    return dt.weekday() >= 5


def start_of_day(dt: datetime) -> datetime:
    """Get the start of the day for a given datetime."""
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(dt: datetime) -> datetime:
    """Get the end of the day for a given datetime."""
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)


def time_between(start: datetime, end: datetime) -> timedelta:
    """Calculate the time difference between two datetimes."""
    return end - start


def seconds_to_human(seconds: int) -> str:
    """Convert seconds to a human-readable duration."""
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}m {seconds % 60}s"
    hours = minutes // 60
    minutes = minutes % 60
    if hours < 24:
        return f"{hours}h {minutes}m"
    days = hours // 24
    hours = hours % 24
    return f"{days}d {hours}h"
