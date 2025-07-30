from handlers.google_calendar import create_event, list_events
from datetime import datetime, timedelta

def schedule_meeting(summary, time_str):
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    end = dt + timedelta(minutes=30)
    return create_event(summary, dt.isoformat(), end.isoformat())

def get_upcoming_events():
    events = list_events()
    return "\n".join(f"{e['summary']} at {e['start'].get('dateTime', e['start'].get('date'))}" for e in events)
