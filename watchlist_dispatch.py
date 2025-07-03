import datetime
import random

def build_watchlist():
    today = datetime.date.today()
    expiry_cutoff = today + datetime.timedelta(days=5)

    # Dummy stock list
    stocks = ['RVNL', 'PRAJIND', 'ADANIENSOL', 'BHARTIARTL', 'SUNPHARMA', 'BANKBARODA']
    lunar_bias = ['Bullish', 'Neutral', 'Bearish']
    watchlist = f"📋 Strategist Watchlist — {today.strftime('%d %b %Y')}\n\n"

    for s in stocks:
        expiry = expiry_cutoff.strftime('%d-%b-%Y')
        bias = random.choice(lunar_bias)
        entry = random.randint(100, 900)
        sl = entry * 0.98
        target = entry * 1.06

        watchlist += f"🔹 {s}\n"
        watchlist += f"- Expiry: {expiry}\n"
        watchlist += f"- Bias: {bias}\n"
        watchlist += f"- Entry: ₹{entry} | Target: ₹{round(target,2)} | SL: ₹{round(sl,2)}\n\n"

    return watchlist
