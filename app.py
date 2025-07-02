from flask import Flask, request
import requests
import os

# ✅ Define the Flask app before using it
app = Flask(__name__)

# Your actual bot token
BOT_TOKEN = '7884759417:AAG_mE6dMrl7Q84PxtW3gpR_jwhrvr6U7jw'
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
        elif text.lower() == '/forecast':
            reply = '📊 Lunar volatility index suggests choppy price action. Avoid overexposure until 11:32am IST when Moon exits Ashlesha. Watch pharma and FMCG sectors.'
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
