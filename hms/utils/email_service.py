import requests

EMAIL_SERVICE_URL = "http://localhost:3000/dev/send-email"


def send_email(trigger, email):
    payload = {
        "trigger": trigger,
        "email": email
    }

    try:
        requests.post(EMAIL_SERVICE_URL, json=payload)
    except Exception as e:
        print("Email service error:", e)