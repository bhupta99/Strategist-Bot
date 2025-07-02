@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').lower()

        # Command responses
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

        # Send reply back to Telegram
        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK'
