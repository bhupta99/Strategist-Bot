import re
from backtestengine import run_backtest
from watchlist_dispatch import build_watchlist

def parse_input(text):
    text = text.lower().strip()

    # Keyword matching
    if 'backtest' in text:
        asset = text.replace('backtest', '').strip()
        return lambda x: run_backtest(asset)
    
    elif 'watchlist' in text or 'watchlistbuild' in text:
        return lambda x: build_watchlist()

    elif re.match(r'^[a-z]{2,4}\d{4,5}.*$', text):  # Option strikes like Nifty25000CE
        return lambda x: f"Running analysis for option: {text}"

    elif text in ['gann', 'kp', 'codex', 'bar']:
        return lambda x: f"Running strategist module: {text}"

    elif re.match(r'^[a-z]{3,}$', text):  # Equity ticker like SBI, TCS
        return lambda x: f"Generating full analysis for stock: {text.upper()}"

    else:
        return None
