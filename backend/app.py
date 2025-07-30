from flask import Flask, request, jsonify
from handlers.google_calendar import list_events, create_event
from pyngrok import ngrok
app = Flask(__name__)

@app.route('/calendar/events', methods=['GET'])
def get_events():
    events = list_events()
    return jsonify(events)

@app.route('/calendar/create', methods=['POST'])
def add_event():
    data = request.get_json()
    summary = data['summary']
    start = data['start']
    end = data['end']
    description = data.get('description', '')
    link = create_event(summary, start, end, description)
    return jsonify({"event_link": link})

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print("public url: ", public_url)
    app.run(debug=True, host='0.0.0.0', port=5000)