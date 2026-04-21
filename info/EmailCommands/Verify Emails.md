# Verify Emails.py

**Path:** `EmailCommands/Verify Emails.py`

**Automation Type:** Email Automation
**Lines:** 109

## Purpose

python verify email with a given regex and add the option to delete emails with the parameters set with the options of processed verification emails, all emails and none

## Library Context

This script is part of the email automation library, providing functions for sending, receiving, and managing email communications.

## Key Features

- Email sending/receiving

## Usage Pattern

Object-oriented - Provides classes and methods with standalone execution capability

## Dependencies

No external dependencies identified.

## Function Descriptions

- __init__ - Parameters: self. Performs a specific operation.
- add_email - Parameters: self, email. Performs a specific operation.
- verify_email - Parameters: self, email. Performs a specific operation.
- process_emails - Parameters: self. Performs a specific operation.
- display_emails - Parameters: self. Performs a specific operation.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### __init__

```python
def __init__(self):
        self.emails = []
        self.verified_emails = []
```

### add_email

```python
def add_email(self, email):
        """Add an email to the list."""
        self.emails.append(email)
```

### verify_email

```python
def verify_email(self, email):
        """
        Verify if the given email address is valid using a regex.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(regex, email):
            return True
        return False
```

### process_emails

```python
def process_emails(self):
        """
        Verify emails in the list and separate verified emails.
        """
        for email in self.emails:
            if self.verify_email(email):
                self.verified_emails.append(email)
```

### display_emails

```python
def display_emails(self):
        """
        Display all emails and verified emails.
        """
        print("All Emails:")
        print(self.emails)
        print("\nVerified Emails:")
        print(self.verified_emails)
```

