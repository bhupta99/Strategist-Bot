from backtestengine import run_backtest
import random

# Define sector → stock mapping
SECTOR_STOCKS = {
    'pharma': ['SUNPHARMA', 'CIPLA', 'DRREDDY', 'BIOCON', 'DIVISLAB'],
    'psu': ['BANKBARODA', 'PNB', 'UNIONBANK', 'IOB', 'CANBK'],
    'it': ['TCS', 'INFY', 'WIPRO', 'HCLTECH', 'TECHM'],
    'auto': ['TATAMOTORS', 'EICHERMOT', 'BAJAJ-AUTO', 'TVSMOTOR', 'ASHOKLEY'],
    'fmcg': ['HINDUNILVR', 'ITC', 'DABUR', 'BRITANNIA', 'MARICO'],
    'infra': ['L&T', 'IRCON', 'RVNL', 'NBCC', 'PNCINFRA']
}

def run_sector_dispatch(sector):
    sector = sector.lower().strip()
    stocks = SECTOR_STOCKS.get(sector, [])

    if not stocks:
        return f"❌ Unknown sector: {sector}. Try pharma, psu, it, auto, fmcg, infra."

    output = f"📊 Strategist Sector Forecast: {sector.title()}\n\n"

    for stock in stocks[:5]:
        entry = random.randint(100, 900)
        target = round(entry * 1.06, 2)
        sl = round(entry * 0.98, 2)
        bias = random.choice(['📈 Bullish', '📉 Bearish', '⚖️ Neutral'])

        backtest = run_backtest(stock)
        output += f"🔹 {stock}\n"
        output += f"- Entry: ₹{entry} | Target: ₹{target} | SL: ₹{sl}\n"
        output += f"- Bias: {bias}\n"
        output += f"{backtest}\n\n"

    return output
