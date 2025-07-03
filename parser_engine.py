import re
from backtestengine import run_backtest
from watchlist_dispatch import build_watchlist
from dispatch_engine import run_dispatch

def parse_input(text):
    text = text.lower().strip()

    # ✅ Stock-level Backtest
    if text.startswith('backtest '):
        asset = text.replace('backtest', '').strip()
        return lambda x: run_backtest(asset)

    # ✅ Full Forecast via Fusion
    elif text.startswith('dispatch '):
        asset = text.replace('dispatch', '').strip()
        return lambda x: run_dispatch(asset)

    # ✅ Watchlist Builder
    elif 'watchlist' in text or 'watchlistbuild' in text:
        return lambda x: build_watchlist()

    # ✅ Sector Dispatch (e.g. PSU Banks, IT, Pharma)
    elif any(sector in text for sector in ['psu', 'pharma', 'it', 'fmcg', 'infra', 'auto']):
        return lambda x: f"📊 Sectoral Forecast for: {text.title()}\n→ (Coming soon: sector-level Gann + KP + backtest fusion)"

    # ✅ Option Strike (e.g. Nifty 24500 CE 11 Jul)
    elif re.search(r'\b(nifty|banknifty|finifty)\b.*\b\d{4,5}\b.*\bce\b|\bpe\b', text):
        return lambda x: f"📈 Option Strike Detected: {text.title()}\n→ (Coming soon: strike-level Gann + OI + KP overlay)"

    # ✅ Module Shortcuts
    elif text in ['gann', 'kp', 'codex', 'bar']:
        return lambda x: f"Running strategist module: {text.upper()}"

    # ✅ Equity Ticker (e.g. SBI, TCS, RVNL)
    elif re.match(r'^[a-z]{3,10}$', text):
        return lambda x: run_dispatch(text)

    # ✅ Fallback Menu if unmatched
    else:
        return lambda x: (
            "🤖 I didn’t recognize that input.\n"
            "Try something like:\n"
            "- `dispatch SBI`\n"
            "- `backtest RVNL`\n"
            "- `watchlistbuild`\n"
            "- `Nifty 24500 CE 11 Jul`\n"
            "- `Pharma sector`"
        )
