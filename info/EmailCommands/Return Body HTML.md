# Return Body HTML.py

**Path:** `EmailCommands/Return Body HTML.py`

**Automation Type:** Email Automation
**Lines:** 97

## Purpose

python email return the body of an email by position as html

## Library Context

This script is part of the email automation library, providing functions for sending, receiving, and managing email communications.

## Key Features

- Email sending/receiving

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `policy`
- `email`
- `imaplib`

## Function Descriptions

No function descriptions available.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### Example Code

```python
import imaplib
import email
from email import policy

def get_email_body_as_html_by_position(username, password, mail_folder, position):
    # Connect to the email server and log in
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Use the appropriate server
    mail.login(username, password)

    #
```

