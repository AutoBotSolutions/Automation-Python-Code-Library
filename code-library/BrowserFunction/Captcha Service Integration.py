import requests

API_KEY = "YOUR_2CAPTCHA_API_KEY"
RECAPTCHA_SITE_KEY = "YOUR_SITE_KEY"
URL = "YOUR_TARGET_URL"


def solve_recaptcha(api_key, site_key, url):
    # Step 1: Request to solve reCAPTCHA
    response = requests.post("http://2captcha.com/in.php", data={
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    })
    request_id = response.json().get("request")

    # Step 2: Poll for solution
    while True:
        resp = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1")
        if resp.json().get("request") == "CAPCHA_NOT_READY":
            time.sleep(5)
            continue
        return resp.json().get("request")


# Example of usage
captcha_token = solve_recaptcha(API_KEY, RECAPTCHA_SITE_KEY, URL)
if captcha_token:
    print(f"Solved reCAPTCHA Token: {captcha_token}")
else:
    print("Failed to solve CAPTCHA.")

######################################################################################
from twilio.rest import Client

ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE = '+1234567890'
TARGET_PHONE = '+0987654321'


def send_sms(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    sms = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=TARGET_PHONE
    )
    return sms.sid


# Example Usage
message = "Hello, this is a test message from Twilio!"
sms_sid = send_sms(message)
print(f"Message sent with SID: {sms_sid}")

######################################################################################
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import base64
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CREDS_FILE = 'path/to/credentials.json'


def send_email(sender, to, subject, message_text):
    creds = Credentials.from_authorized_user_file(CREDS_FILE, SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    mime_message = MIMEText(message_text)
    mime_message['to'] = to
    mime_message['subject'] = subject
    raw = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    body = {'raw': raw}
    message = service.users().messages().send(userId=sender, body=body).execute()
    return message


# Example Usage
email = send_email("me", "recipient@example.com", "Testing Gmail API", "Hello from Gmail API!")
print(f"Email sent: {email}")