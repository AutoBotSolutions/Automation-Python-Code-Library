# Return Body.py

**Path:** `EmailCommands/Return Body.py`

**Automation Type:** Email Automation
**Lines:** 84

## Purpose

python return the email body of an email at specified by the position

## Library Context

This script is part of the email automation library, providing functions for sending, receiving, and managing email communications.

## Key Features

- Email sending/receiving

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `default`
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
from email.policy import default

def get_email_body_at_position(position, email_server, email_user, email_password, mailbox="INBOX"):
    try:
        # Connect to the email server
        mail = imaplib.IMAP4_SSL(email_server)
        mail.login(email_user, email_passwo
```

