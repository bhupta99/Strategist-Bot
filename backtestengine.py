import random

def run_backtest(asset):
    # Dummy example — replace with full logic tied to historical database
    history = [
        {'date': '2024-07-12', 'entry': 102, 'exit': 108, 'sl': 100},
        {'date': '2024-09-14', 'entry': 110, 'exit': 106, 'sl': 108},
        {'date': '2024-10-04', 'entry': 118, 'exit': 124, 'sl': 115}
    ]

    output = f"📊 Backtest Report for: {asset.upper()}\n"
    hits, fails = 0, 0

    for h in history:
        move = h['exit'] - h['entry']
        pct = round((move / h['entry']) * 100, 2)
        result = "✅ Target Hit" if h['exit'] > h['entry'] else "❌ SL Hit"
        if result.startswith("✅"): hits += 1
        else: fails += 1

        output += f"- {h['date']}: Entry ₹{h['entry']} → Exit ₹{h['exit']} ({pct}%) → {result}\n"

    bias = "📈 Bullish" if hits > fails else "📉 Bearish"
    output += f"\n📌 Bias Summary: {bias} ({hits} wins / {fails} fails)"

    # Predictive Setup (Dummy)
    entry = random.randint(100, 120)
    target = entry * 1.06
    sl = entry * 0.98
    output += f"\n→ Suggested Entry: ₹{entry} | Target: ₹{round(target,2)} | SL: ₹{round(sl,2)}\n"

    return output
