from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Replace with your actual bot token
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

        # Base commands
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

        elif text == '/signal':
            # Strategic signal dispatch (Bayer Rule #22)
            rule_number = "22"
            rule_name = "Mercury Rx conjunct Sun"
            condition = "Retrograde Mercury passes over the Sun during Ashlesha transit"
            description = (
                "Bayer noted this configuration often triggers emotional market reversals, "
                "especially in speculative sectors within 1–3 trading sessions."
            )
            next_trigger = "July 11, 2025"
            codex_setup = "Bearish Shark PRZ at Nifty 23,637 with RSI divergence below 50EMA"
            gann_level = "Square of 9 resistance matched at angle 45°: 23,637"
            lunar_aspect = "Moon in Ashlesha + combust Mars = volatile intraday bias"
            bramesh_sector = "FMCG, Pharma and Index-heavy stocks likely to react sharply"
            stock = "Sun Pharma"
            entry = "₹1,145"
            stop_loss = "₹1,138"
            target = "₹1,180"
            confidence = "Medium-High"

            historical_block = (
                "🕰️ Historical Bayer Rule #22 Activations:\n"
                "- Avg Move: ±2.0%, ~440 pts over 2 bars\n"
                "- Directional Bias: 67% Bearish\n"
                "- SL Hit: 3 times | Target Hit: 6 times\n"
                "- Avg Point Change: ±432 pts"
            )

            reply = (
                f"🔍 CodexABCD-Aligned Bayer-Gann Signal\n"
                f"📜 Rule #{rule_number}: {rule_name}\n"
                f"⚙️ Condition: {condition}\n"
                f"📖 Description: {description}\n\n"
                f"📊 Gann Level: {gann_level}\n"
                f"🌌 Astro Setup: {lunar_aspect}\n"
                f"🧾 Bramesh Sector Bias: {bramesh_sector}\n"
                f"🌀 Codex Setup: {codex_setup}\n\n"
                f"💹 Stock Pick: {stock}\n"
                f"🎯 Entry: {entry} | SL: {stop_loss} | Target: {target} | Confidence: {confidence}\n\n"
                f"{historical_block}\n\n"
                f"📅 Next Activation: {next_trigger}\n"
                f"📬 Signal dispatched by strategist bot • AI + Astro + Harmonic fusion"
            )

        else:
            reply = f'📩 Echo: You said "{text}" — strategist is listening.'

        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
