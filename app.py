from flask import Flask, request
import requests
import os

app = Flask(__name__)

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
        text = data['message'].get('text', '').strip().lower()

        if text == '/start':
            reply = '🚀 Strategist Bot activated. Send /signal for astro-harmonic alerts or /sectorwatch to check today\'s lunar-aligned sectors.'

        elif text == 'hi':
            reply = 'Hello from Strategist Bot 👋'

        elif text in ['/forecast', 'forecast']:
            reply = '📊 Forecast: Volatility expected near Ashlesha-to-Magha lunar transition. Pharma and FMCG sectors may show momentum post 11:32am IST.'

        elif text in ['/astro', 'astro']:
            reply = '🌕 Astro Trend: Moon in Ashlesha, combust Mars nearby. Avoid leveraged trades. Favor large caps.'

        elif text in ['/expiry', 'expiry']:
            reply = '📅 Expiry Signal: Nifty resistance near Gann 19802. Watch for intraday reversal zone from 12:15–13:05 IST.'

        elif text in ['/volatility', 'volatility']:
            reply = '🌌 Volatility Watch: High nakshatra density. Magha ingress eases pressure. Breakout bias likely post 11:30am.'

        elif text in ['/signal', 'signal']:
            reply = (
                "🔍 CodexABCD-Aligned Bayer-Gann Signal\n"
                "📜 Rule #22: Mercury Rx conjunct Sun\n"
                "⚙️ Condition: Retrograde Mercury passes over Sun in Ashlesha\n"
                "📖 Bayer notes speculative reversals within 1–3 bars\n\n"
                "📊 Gann Level: Nifty 23,637 matches Square of 9 45° angle\n"
                "🌌 Astro Setup: Moon in Ashlesha, combust Mars\n"
                "🧾 Bramesh Bias: Pharma, FMCG likely to reverse intraday\n"
                "🌀 Codex Setup: Bearish Shark PRZ + RSI divergence\n\n"
                "💹 Stock: Sun Pharma\n"
                "🎯 Entry: ₹1,145 | SL: ₹1,138 | Target: ₹1,180 | Confidence: Medium-High\n\n"
                "🕰️ History: Avg ±2.0%, ~432 pts, 2 bars\n"
                "📅 Next Trigger: July 11, 2025\n"
                "📬 Signal dispatched • AI + Astro + Harmonics"
            )

        elif text == '/signal14':
            reply = (
                "📜 Bayer Rule #14: Venus crosses 1°9'13\" longitude\n"
                "🧾 Bramesh: Consumer stocks & Bank Nifty often show surge\n"
                "💹 Sector Focus: Financials, FMCG\n"
                "🎯 Sample Stock: HUL — Buy ₹2,634 | SL ₹2,612 | Target ₹2,695\n"
                "📊 Gann Cluster: Nifty shows seasonal square hit\n"
                "📬 Historical Accuracy: 78% target hit last 9 events\n"
                "📅 Next Activation: Aug 9, 2025"
            )

        elif text == '/signal33':
            reply = (
                "📜 Bayer Rule #33: Mars crosses 16°55'46\"\n"
                "🧾 Bramesh: Energy & Metal stocks prone to reversals\n"
                "💹 Sector Focus: Oil, Steel\n"
                "🎯 Sample: Tata Steel — Short ₹145.20 | SL ₹148.50 | Target ₹140.10\n"
                "📊 CodexABCD: Diamond breakdown under 50EMA\n"
                "📅 Next Activation: Sep 2, 2025"
            )

        elif text == '/sectorwatch':
            reply = (
                "📊 Sector Watch:\n"
                "🌕 Astro Bias: Magha dominance favors PSU Banks\n"
                "📐 Gann Pressure: FMCG & Pharma near angular supports\n"
                "🌀 CodexABCD Setup: Bearish divergence in Energy index\n"
                "🔮 Lunar Volatility: Midcap sector prone to intraday spikes"
            )

        elif text == '/gannmap':
            reply = (
                "📐 Gann Map Guide:\n"
                "◽ Square of 9 → 45° angle = resistance zone\n"
                "🔺 Emblem Logic → July 11 is emblem pushback date\n"
                "🧭 Seasonal Squaring: Post-solstice volatility window"
            )

        elif text == '/astrotrend':
            reply = (
                "🌌 Planetary Status:\n"
                "- Moon: Ashlesha → Magha transition (volatile)\n"
                "- Mars: Combust under Sun\n"
                "- Mercury: Retro
