@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').lower()

        if text == 'hi':
            reply = 'Hello from Strategist Bot 👋'

        elif text == '/forecast':
            # Sample response — you can replace this with live astro-market logic
            reply = '📊 Lunar volatility index suggests choppy price action. Avoid overexposure until 11:32am IST when Moon exits Ashlesha. Watch pharma and FMCG sectors.'

        else:
            reply = f'You said: {text}'

        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK'
