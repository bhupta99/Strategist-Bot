import re
import random

def run_strike_dispatch(text):
    text = text.upper().strip()

    # Extract index, strike, and option type
    match = re.search(r'(NIFTY|BANKNIFTY|FINIFTY)\s*(\d{4,5})\s*(CE|PE)', text)
    if not match:
        return "❌ Could not parse strike. Try: Nifty 24500 CE"

    index, strike, opt_type = match.groups()
    strike = int(strike)

    # Simulated Gann angle logic
    gann_base = strike - 90 if opt_type == 'PE' else strike - 110
    gann_res = strike + 60
    gann_angle = "45°" if (strike % 90) < 10 else "135°"

    # Simulated KP sub-lord logic
    kp_sublord = random.choice(['Mercury', 'Venus', 'Mars', 'Jupiter'])
    kp_bias = "Bullish" if kp_sublord in ['Venus', 'Jupiter'] else "Bearish"

    # Simulated OI zone
    oi_resistance = strike + 50
    oi_support = strike - 50

    # Entry/SL/Target logic
    entry = strike + 20 if opt_type == 'CE' else strike - 20
    sl = entry - 30
    target = entry + 60
    bias = "📈 Bullish" if opt_type == 'CE' else "📉 Bearish"

    return (
        f"📊 Strategist Strike Forecast\n"
        f"───────────────\n"
        f"🔹 Index: {index}\n"
        f"🔹 Strike: {strike} {opt_type}\n"
        f"🔹 Bias: {bias} ({kp_bias} by KP)\n\n"
        f"📐 Gann Angle: {gann_angle} from ₹{gann_base}\n"
        f"🔮 KP Sub-lord: {kp_sublord}\n"
        f"📊 OI Zones: Resistance ₹{oi_resistance} | Support ₹{oi_support}\n\n"
        f"🎯 Entry: ₹{entry}\n"
        f"🛡️ SL: ₹{sl}\n"
        f"🎯 Target: ₹{target}\n"
    )
