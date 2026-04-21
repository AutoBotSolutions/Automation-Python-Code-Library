# time_utils.py

**Path:** `CodeLibrary/src/codelibrary/time_utils.py`

**Automation Type:** General Automation
**Lines:** 123

## Purpose

Time and date manipulation utilities.

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `datetime.datetime`
- `datetime.timedelta`
- `typing.Optional`
- `typing.List`
- `time`

## Functions

### now

Get the current datetime.

### now_timestamp

Get the current Unix timestamp.

### datetime_to_timestamp

**Parameters:** dt

Convert a datetime to Unix timestamp.

### timestamp_to_datetime

**Parameters:** timestamp

Convert a Unix timestamp to datetime.

### format_datetime

**Parameters:** dt, format_str

Format a datetime as a string.

### parse_datetime

**Parameters:** date_str, format_str

Parse a datetime string into a datetime object.

### add_days

**Parameters:** dt, days

Add days to a datetime.

### add_hours

**Parameters:** dt, hours

Add hours to a datetime.

### add_minutes

**Parameters:** dt, minutes

Add minutes to a datetime.

### time_ago

**Parameters:** dt

Get a human-readable time ago string.

... and 6 more functions

## Code Examples

### now

```python
def now() -> datetime:
    """Get the current datetime."""
    return datetime.now()
```

### now_timestamp

```python
def now_timestamp() -> float:
    """Get the current Unix timestamp."""
    return time.time()
```

### datetime_to_timestamp

```python
def datetime_to_timestamp(dt: datetime) -> float:
    """Convert a datetime to Unix timestamp."""
    return dt.timestamp()
```

