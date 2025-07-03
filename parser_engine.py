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

    # ✅ Module Shortcuts
    elif text in ['gann', 'kp', 'codex', 'bar']:
        return lambda x: f"Running strategist module: {text.upper()}"

    # ✅ Option Strike (e.g. Nifty 24500 CE)
    elif re.search(r'\bce\b|\bpe\b', text):
        return lambda x: f"Analyzing option strike: {text}"

    # ✅ Equity Ticker (e.g. SBI, TCS)
    elif re.match(r'^[a-z]{3,}$', text):
        return lambda x: run_dispatch(text)  # Default to full fusion

    # ✅ Fallback Menu if unmatched
    else:
        return None
