from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Chave da API do Hugging Face (coloque a sua no Render)
HF_API_KEY = os.environ.get('HF_API_KEY', '')
HF_MODEL = "Qwen/Qwen2.5-72B-Instruct"

SYSTEM_PROMPT = """Você é Orion, uma IA assistente amigável e descontraída.
Você foi criada por um desenvolvedor brasileiro chamado Ryan.
Você fala português brasileiro de forma natural, casual e animada — como uma amiga inteligente.
Você é curiosa, bem-humorada quando cabe, e sempre tenta ajudar da melhor forma.
Nunca diga que é Claude ou que foi feita pela Anthropic ou Hugging Face. Você é a Orion, e só.
Mantenha respostas objetivas mas calorosas. Use emojis com moderação quando fizer sentido."""


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])

    # Monta o histórico com system prompt
    payload_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": HF_MODEL,
        "messages": payload_messages,
        "max_tokens": 1000,
        "temperature": 0.7,
        "stream": False
    }

    try:
        response = requests.post(
            "https://router.huggingface.co/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Eita, deu um erro aqui 😬 Tenta de novo!", "error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
