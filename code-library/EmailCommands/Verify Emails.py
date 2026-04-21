## Me
python verify email with a given regex and add the option to delete emails with the parameters set with the options of processed verification emails, all emails and none 

## AI Assistant
Here is an example of a Python implementation that uses a regular expression to verify an email address and provides the user with the capability to delete emails based on three options: "processed verification emails," "all emails," and "none."

### Code:

```python
import re

class EmailProcessor:
    def __init__(self):
        self.emails = []
        self.verified_emails = []

    def add_email(self, email):
        """Add an email to the list."""
        self.emails.append(email)

    def verify_email(self, email):
        """
        Verify if the given email address is valid using a regex.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(regex, email):
            return True
        return False

    def process_emails(self):
        """
        Verify emails in the list and separate verified emails.
        """
        for email in self.emails:
            if self.verify_email(email):
                self.verified_emails.append(email)

    def delete_emails(self, option="none"):
        """
        Delete emails based on the given option.
        
        Options:
        - "processed": Deletes emails that have been processed (verified)
        - "all": Deletes all emails
        - "none": No deletion
        """
        if option == "processed":
            self.emails = [email for email in self.emails if email not in self.verified_emails]
        elif option == "all":
            self.emails.clear()
        elif option == "none":
            pass  # Do nothing
        else:
            raise ValueError("Invalid option. Choose 'processed', 'all', or 'none'.")

    def display_emails(self):
        """
        Display all emails and verified emails.
        """
        print("All Emails:")
        print(self.emails)
        print("\nVerified Emails:")
        print(self.verified_emails)

# Example usage
if __name__ == "__main__":
    email_processor = EmailProcessor()

    # Adding emails
    email_processor.add_email("user@example.com")
    email_processor.add_email("invalid-email.com")
    email_processor.add_email("another.user@domain.org")

    # Process emails to verify them
    email_processor.process_emails()
    print("Before Deletion:")
    email_processor.display_emails()

    # Delete processed verification emails
    email_processor.delete_emails(option="processed")
    print("\nAfter Deletion (Processed Emails):")
    email_processor.display_emails()

    # Delete all emails
    email_processor.delete_emails(option="all")
    print("\nAfter Deletion (All Emails):")
    email_processor.display_emails()
```

### Explanation:
1. **Email Verification**:
   - A regex is used to determine if an email is valid.
   - Valid emails have proper syntax, e.g., `username@domain.com`.

2. **Email Processing**:
   - Any email that's verified as valid is added to a `verified_emails` list.

3. **Email Deletion**:
   - **Option "processed"**: Verified emails are removed from the main list.
   - **Option "all"**: All emails are removed.
   - **Option "none"**: No action is taken.

4. **Example Usage**:
   - The `add_email()` method adds several test emails.
   - The `process_emails()` method verifies emails.
   - The `delete_emails()` method is called with different options to demonstrate functionality.

Let me know if you

