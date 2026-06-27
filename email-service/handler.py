import json
import smtplib
from email.mime.text import MIMEText
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_email(event, context):

    body = json.loads(event["body"])

    trigger = body["trigger"]
    recipient = body["email"]

    if trigger == "SIGNUP_WELCOME":
        subject = "Welcome to HMS"
        message = "Welcome! Your account has been created successfully."

    elif trigger == "BOOKING_CONFIRMATION":
        subject = "Appointment Confirmed"
        message = "Your appointment has been booked successfully."

    else:
        subject = "Hospital Management System"
        message = "Notification"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email sent successfully"
        })
    }