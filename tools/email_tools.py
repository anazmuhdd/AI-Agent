from gmail_reader.mail_read import authenticate, get_primary_messages
service = authenticate()

def read_unread_emails():
    try:
        get_primary_messages(service, MAX_RESULTS=3)
        return "Fetched unread emails and stored job applications."
    except Exception as e:
        return f"Email fetch error: {str(e)}"
