## Me
python return the body text of the email specified by the position

## AI Assistant
If you're working to extract the body text of a specific email (based on its position in a list, for example), here's the general logic you might need. The solution would depend on how you're accessing and processing the emails. Here's an example code snippet that demonstrates how to extract the body of an email based on its position from a list of emails.

### Example Code:
```python
import email
from email.policy import default

def get_email_body(emails, position):
    """
    Retrieves the body text of the email specified by its position.

    Args:
        emails (list): A list of email raw strings or email.message.Message objects.
        position (int): The position of the email in the list (1-based index).

    Returns:
        str: The body text of the email or an error if the position is invalid.
    """
    if position < 1 or position > len(emails):
        return "Invalid email position. Please provide a valid index."
    
    # Get the email at the given position (convert to 0-based index)
    email_data = emails[position - 1]

    # If it's a raw string, parse it into an email.message.Message object
    if isinstance(email_data, str):
        email_message = email.message_from_string(email_data, policy=default)
    elif isinstance(email_data, email.message.EmailMessage):
        email_message = email_data
    else:
        return "Invalid email format."

    # Extract the body part of the email
    body = ""
    if email_message.is_multipart():
        # Iterate through the parts to find the text/plain content
        for part in email_message.iter_parts():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
    else:
        # If it's not a multipart message, simply get the payload
        body = email_message.get_content()

    return body or "No body content found."

# Example usage
emails = [
    # Add raw email strings (or email.message.Message objects) here
]
position = 1  # Specify the position of the email to extract
print(get_email_body(emails, position))
```

### Explanation:
1. **Input**:
   - A list called `emails` that contains raw strings or parsed email objects (`email.message.Message`).
   - The `position` of the email to extract (1-based index for user-friendliness).

2. **Validation**:
   - The function ensures the position is a valid index for the given list of emails.

3. **Body Extraction**:
   - If the email is multipart (e.g., HTML and plain text), it iterates through the parts of the message to locate the `text/plain` content type.
   - Otherwise, it directly extracts the payload.

4. **Result**:
   - The body text of the email is returned. If no body is found, it returns a fallback message.

### Notes:
- Adjust the input `emails` to contain the raw email content or parsed email objects.
- If emails are being fetched from an external system (like IMAP), you'll need appropriate libraries (`imaplib` or `imap_tools`) to load them.
- Modify this base solution per your exact requirements. Let me know if you need help connecting this functionality to your email source!

