# time_utils.py

**Path:** `CodeLibrary/src/codelibrary/time_utils.py`

**Lines:** 123
**Size:** 3453 bytes

## Description

Time and date manipulation utilities.

## Imports

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

### get_date_range

**Parameters:** start_date, end_date

Get a list of datetimes for each day in a date range.

### is_weekend

**Parameters:** dt

Check if a datetime falls on a weekend.

### start_of_day

**Parameters:** dt

Get the start of the day for a given datetime.

### end_of_day

**Parameters:** dt

Get the end of the day for a given datetime.

### time_between

**Parameters:** start, end

Calculate the time difference between two datetimes.

... and 1 more functions

