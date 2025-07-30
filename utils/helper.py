def is_meeting_request(text):
    return any(word in text.lower() for word in ["schedule", "book", "meeting"])

def extract_time(text):
    import re
    match = re.search(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})', text)
    if match:
        return f"{match.group(1)} {match.group(2)}"
    return None
