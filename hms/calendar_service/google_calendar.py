from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def create_calendar_event(
    access_token,
    doctor_email,
    patient_email,
    start_datetime,
    end_datetime,
    doctor_name,
    patient_name
):

    creds = Credentials(token=access_token)

    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": f"Appointment with Dr. {doctor_name}",
        "description": f"Patient: {patient_name}",
        "start": {
            "dateTime": start_datetime.isoformat(),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": end_datetime.isoformat(),
            "timeZone": "UTC",
        },
        "attendees": [
            {"email": doctor_email},
            {"email": patient_email},
        ],
    }

    service.events().insert(
        calendarId="primary",
        body=event
    ).execute()