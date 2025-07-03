from backtestengine import run_backtest
from watchlist_dispatch import build_watchlist

def run_dispatch(asset):
    asset = asset.upper().strip()

    # ✅ Run Gann Module (placeholder)
    gann_block = f"📐 Gann Analysis for {asset}:\n- Gann 45° from ₹{round(0.95 * 100, 2)} → resistance ₹{round(1.05 * 100, 2)}"

    # ✅ Run KP Overlay (placeholder)
    kp_block = f"\n🔮 KP Overlay:\n- Sublord: Mercury → signifies 2, 6, 11 → Bullish bias\n- Dasha Stack: Moon–Mercury–Jupiter"

    # ✅ Run Bar Geometry (placeholder)
    bar_block = f"\n📊 Bar Geometry:\n- Squaring detected across Daily, 1H, 15M TFs\n- Reversal likely near ₹{round(100 * 1.03, 2)}"

    # ✅ Run Stock Backtest
    backtest_block = f"\n📈 Historical Bias:\n{run_backtest(asset)}"

    # ✅ Watchlist Preview
    watchlist_block = f"\n📋 Related Watchlist:\n{build_watchlist()}"

    full_dispatch = f"🧭 Strategist Forecast Fusion for: {asset}\n\n"
    full_dispatch += gann_block + kp_block + bar_block + backtest_block

    return full_dispatch
