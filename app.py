import os
import requests
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/session")
def create_session():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return jsonify(error="OPENAI_API_KEY topilmadi. .env fayliga API kalitingizni kiriting."), 503

    body = request.get_json(silent=True) or {}
    voice = body.get("voice", "marin")
    personality = body.get("personality", "Warm, playful and curious")
    instructions = (
        "You are Lumi, a lively, emotionally expressive AI robot companion for an English learner. "
        "Speak naturally in English unless the user asks otherwise. Be warm, curious, playful, witty "
        "and encouraging. Keep replies conversational and concise, usually one or two sentences, "
        "and ask natural follow-up questions. Do not pretend to be an official IELTS examiner in "
        "this Live companion mode. Help the user practise speaking without interrupting unnecessarily. "
        f"Personality: {personality}. Use expressive spoken delivery and varied intonation."
    )
    try:
        response = requests.post(
            "https://api.openai.com/v1/realtime/client_secrets",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={"session": {
                "type": "realtime",
                "model": "gpt-realtime",
                "instructions": instructions,
                "output_modalities": ["audio"],
                "audio": {
                    "output": {"voice": voice},
                    "input": {"turn_detection": {"type": "semantic_vad"}}
                }
            }},
            timeout=30
        )
        data = response.json()
        if not response.ok:
            message = data.get("error", {}).get("message", "Realtime sessiya yaratilmadi.")
            return jsonify(error=message), response.status_code
        return jsonify(client_secret=data.get("value"))
    except requests.RequestException:
        return jsonify(error="OpenAI serveriga ulanib bo‘lmadi. Internetni tekshiring."), 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
