## Me
python return email recipient at given position

## AI Assistant
To return an email recipient at a given position in Python, you would generally start with a list or string of recipients. Here's an example of how you could implement this:

### Example Code to Return Recipient at Position
```python
def get_recipient_at_position(recipients, position):
    """
    Get the email recipient at the specified position in the list.

    Args:
    - recipients (list): List of email recipients as strings.
    - position (int): Index (1-based) of the recipient to return.

    Returns:
    - str: The email address at the given position.
    - None: If the position is out of range.
    """
    if position < 1 or position > len(recipients):
        return None
    return recipients[position - 1]


# Example Usage
recipients_list = ["alice@example.com", "bob@example.com", "charlie@example.com"]
position = 2
recipient = get_recipient_at_position(recipients_list, position)
print(f"Recipient at position {position}: {recipient}")
```

### How the Code Works:
1. The function `get_recipient_at_position` accepts a list of email recipients (`recipients`) and a 1-based position (`position`).
2. It checks the bounds of the position (`< 1` or greater than the list length).
3. If valid, it returns the recipient by converting the 1-based position into a 0-based index.
4. If invalid, it returns `None`.

---

### Example Output:
If `recipients_list = ["alice@example.com", "bob@example.com", "charlie@example.com"]` and `position = 2`, the output will be:

```
Recipient at position 2: bob@example.com
```

Let me know if you'd like further customization or if you intend to process recipients from a specific text format!

