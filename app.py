from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Replace this with your actual bot token from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

@app.route('/')
def home():
    return 'Strategist Bot is live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        # Basic response logic
        if text.lower() == 'hi':
            reply = 'Hello from Strategist Bot 👋'
        else:
            reply = f'You said: {text}'

        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
