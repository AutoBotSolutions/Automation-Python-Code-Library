using selenium set proxy credentials

## Me
using selenium set proxy credentials

## AI Assistant
To set proxy settings, including credentials, in Selenium, you can use the following method. This example demonstrates how to configure a proxy and pass the username and password:
### Example Code for Setting Proxy with Authentication
``` python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define proxy settings
proxy_host = "proxy.example.com"
proxy_port = "8080"
proxy_username = "your_username"
proxy_password = "your_password"


# Create a Proxy extension to handle username and password
def create_proxy_extension(proxy_host, proxy_port, proxy_username, proxy_password):
    proxy_manifest = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
              singleProxy: {{
                scheme: "http",
                host: "{proxy_host}",
                port: parseInt({proxy_port})
              }},
              bypassList: []
            }}
    }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{proxy_username}",
                password: "{proxy_password}"
            }}
        }};
    }}

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {{urls: ["<all_urls>"]}},
        ['blocking']
    );
    """

    import os
    import zipfile

    plugin_file = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", proxy_manifest)
        zp.writestr("background.js", background_js)

    return plugin_file


# Create the proxy plugin with credentials
proxy_plugin = create_proxy_extension(proxy_host, proxy_port, proxy_username, proxy_password)

# Set Chrome options
chrome_options = Options()
chrome_options.add_extension(proxy_plugin)

# Instantiate WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Use the WebDriver instance as usual
driver.get("http://www.google.com")

# Close the driver
driver.quit()
```


