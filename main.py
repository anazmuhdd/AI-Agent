from flask import Flask, request, jsonify
from agent_runner import run_agent

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    question = data.get("message")
    if not question:
        return jsonify({"error": "No message provided"}), 400
    reply = run_agent(question)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
