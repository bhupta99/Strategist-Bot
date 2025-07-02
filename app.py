from flask import Flask, request
import requests
import os

# ✅ Define the Flask app first
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
        text = data['message'].get('text', '').lower()

        if text == 'hi':
            reply = 'Hello from Strategist Bot 👋'
        elif text == '/forecast':
            reply = '📊 Forecast: Volatility expected near Ashlesha-to-Magha lunar transition. Pharma and FMCG sectors may show momentum post 11:32am IST.'
        elif text == '/astro':
            reply = '🌕 Astro Alert: Moon in Ashlesha, combust Mars nearby. Avoid leveraged trades. Favor large caps over speculative midcaps.'
        elif text == '/expiry':
            reply = '📅 Expiry Signal: Nifty resistance at Gann 19802. Watch for intraday reversals between 12:15–13:05 IST. Avoid options decay zones.'
        elif text == '/volatility':
            reply = '🌌 Volatility Watch: Nakshatra density high till Moon enters Magha. Astral pressure easing after 11:32am. Favor breakout plays post-lunch.'
        else:
            reply = f'📩 Echo: You said \"{text}\" — strategist is listening.'

        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
