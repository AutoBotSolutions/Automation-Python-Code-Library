## Me
python change text casing

## AI Assistant
To change the casing of text in Python, you can use string methods like:

1. `str.upper()` - Converts all characters in the string to uppercase.
2. `str.lower()` - Converts all characters in the string to lowercase.
3. `str.title()` - Converts the first character of each word to uppercase and the rest to lowercase.
4. `str.capitalize()` - Capitalizes the first character of the string and makes the rest lowercase.
5. `str.swapcase()` - Swaps the case for all characters (e.g., lowercase becomes uppercase, and vice versa).

Below is some example code demonstrating these methods:

```python
# Example string
text = "hello World! Let's Change the TEXT casing."

# Changing text casing
uppercase = text.upper()
lowercase = text.lower()
title_case = text.title()
capitalized = text.capitalize()
swapped_case = text.swapcase()

print("Original:", text)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Title Case:", title_case)
print("Capitalized:", capitalized)
print("Swapped Case:", swapped_case)
```

Output:
```
Original: hello World! Let's Change the TEXT casing.
Uppercase: HELLO WORLD! LET'S CHANGE THE TEXT CASING.
Lowercase: hello world! let's change the text casing.
Title Case: Hello World! Let'S Change The Text Casing.
Capitalized: Hello world! let's change the text casing.
Swapped Case: HELLO wORLD! lET'S cHANGE THE text CASING.
```

Let me know if you need to implement this into your current project!

