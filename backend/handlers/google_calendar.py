import datetime
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying SCOPES, delete the token.json
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=5000, access_type='offline', prompt='consent')
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    service = build("calendar", "v3", credentials=creds)
    return service

def list_events():
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now, maxResults=50, singleEvents=True,
        orderBy='startTime').execute()
    print("datetime", now)
    events = events_result.get('items', [])
    return events

def create_event(summary, start_time, end_time, description=''):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')
