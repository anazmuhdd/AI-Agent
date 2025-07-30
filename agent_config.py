from langchain.agents import Tool
from tools.calendar_tools import schedule_meeting, get_upcoming_events
from tools.email_tools import read_unread_emails

tools = [
    Tool(
        name="ScheduleMeeting",
        func=lambda q: schedule_meeting("Meeting", q),
        description="Schedule a meeting. Input must be 'YYYY-MM-DD HH:MM'."
    ),
    Tool(
        name="GetUpcomingEvents",
        func=lambda _: get_upcoming_events(),
        description="Get list of upcoming calendar events."
    ),
    Tool(
        name="CheckUnreadEmails",
        func=lambda _: read_unread_emails(),
        description="Read unread Gmail messages and log job applications."
    )
]
