## AI Assistant
Here are examples of **HTTP GET and POST** requests in Python using the most commonly used `requests` library:

### HTTP GET Request Example:

```python
import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request to the API
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("GET Request successful. Data received:")
    print(data)  # Prints the fetched data
else:
    print(f"GET Request failed with status code: {response.status_code}")
```

---

### HTTP POST Request Example:

```python
import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Define the data to be sent as payload
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Make a POST request to the API
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 201:  # HTTP status code 201 indicates creation
    # Parse the JSON response
    data = response.json()
    print("POST Request successful. Data received:")
    print(data)  # Prints the server's response
else:
    print(f"POST Request failed with status code: {response.status_code}")
```

---

### Notes:
1. Replace the URLs (`https://jsonplaceholder.typicode.com/posts`) with actual API endpoints for your use case.
2. Ensure you install the `requests` library before running the code.
```shell script
pip install requests
```
3. The above example demonstrates simple payloads. For more complex data, you can explore sending files, authentication headers, etc.

Would you like a more advanced example or details about handling headers, authentication, or error handling? Let me know!

