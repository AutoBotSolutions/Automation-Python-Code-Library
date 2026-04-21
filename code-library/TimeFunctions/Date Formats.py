## Me
python date formats

## AI Assistant
In Python, the **date and time** can be manipulated using the `datetime` module. To display or parse dates, you can use various **format codes**. Below is a guide for frequently used **date formats**.

### Common Date Format Codes
Here are the standard format codes used with `strftime()` (to format) and `strptime()` (to parse) in the `datetime` module:

#### Year
- `%Y` → Full year (e.g., `2023`)
- `%y` → Two-digit year (e.g., `23`)

#### Month
- `%B` → Full month name (e.g., `October`)
- `%b` → Abbreviated month name (e.g., `Oct`)
- `%m` → Month as a zero-padded decimal number (e.g., `01` for January)

#### Day
- `%d` → Day of the month as zero-padded (e.g., `01`, `31`)
- `%a` → Abbreviated weekday name (e.g., `Mon`)
- `%A` → Full weekday name (e.g., `Monday`)
- `%w` → Weekday as a decimal number (`0` for Sunday → `6` for Saturday)
- `%j` → Day of the year as zero-padded (e.g., `001` through `366`)

#### Time
- `%H` → Hour (24-hour clock) as zero-padded (e.g., `00`, `23`)
- `%I` → Hour (12-hour clock) as zero-padded (e.g., `01`, `12`)
- `%p` → AM or PM
- `%M` → Minute as zero-padded (e.g., `00`, `59`)
- `%S` → Second as zero-padded (e.g., `00`, `59`)
- `%f` → Microsecond as zero-padded (e.g., `000000`, `999999`)

#### Time Zone
- `%z` → UTC offset in the form ±HHMM (e.g., `+0000`, `-0500`)
- `%Z` → Time zone name (e.g., `UTC`, `EST`)

#### Miscellaneous
- `%c` → Locale’s date and time representation (e.g., `Wed Oct 4 09:30:12 2023`)
- `%x` → Locale’s date representation (e.g., `10/04/23` in MM/DD/YY format)
- `%X` → Locale’s time representation (e.g., `09:30:12`)
- `%%` → A literal `%` character

---

### Examples of Formatting Dates

```python
from datetime import datetime

# Current date and time
now = datetime.now()

# Format as "Year-Month-Day Hour:Minute:Second"
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # e.g., "2023-10-04 14:45:00"

# Full weekday name, Month name, and Day
verbose_format = now.strftime("%A, %B %d, %Y")
print(verbose_format)  # e.g., "Wednesday, October 04, 2023"
```

---

### Parsing Strings into Dates

You can use `strptime()` to parse a string into a `datetime` object using matching format codes.

```python
from datetime import datetime

date_string = "2023-10-04 14:45:00"
# Parse into a datetime object
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # Outputs: datetime.datetime(2023, 10, 4, 14, 45)
```

---

### Preset ISO and RFC Formats

For common cases, Python provides some predefined formats:
- `datetime.date.isoformat()` → Formats as `YYYY-MM-DD`.
- `datetime.datetime.isoformat()` → Formats as `YYYY-MM-DDTHH:MM:SS`.
- `datetime.datetime.strptime()` can match ISO (`%Y-%m-%dT%H:%M:%S`).

Example:
```python
from datetime import datetime

now = datetime.now()
print(now.isoformat())  # "2023-10-04T14:45:00"
```

Let me know if you need further examples or clarification about Python date formatting!

