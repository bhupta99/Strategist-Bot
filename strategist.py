import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from parser_engine import parse_input
from telepush import push_dispatch

# 🔐 Replace these with your actual values
TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE'
USER_ID = 'PASTE_YOUR_TELEGRAM_USER_ID_HERE'

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📐 Gann Geometry", callback_data='gann')],
        [InlineKeyboardButton("🔮 KP Overlay", callback_data='kp')],
        [InlineKeyboardButton("📊 Codex Harmonics", callback_data='codex')],
        [InlineKeyboardButton("📈 Bar Geometry", callback_data='bar')],
        [InlineKeyboardButton("📅 Watchlist Builder", callback_data='watchlist')],
        [InlineKeyboardButton("📦 Sector Backtest", callback_data='sectorbacktest')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🧭 Strategist Console Activated — Choose your module:", reply_markup=reply_markup)

def handle_input(update, context):
    user_input = update.message.text.strip()
    action = parse_input(user_input)
    if action:
        result = action(user_input)
        push_dispatch(update.message.chat_id, result, TOKEN)
    else:
        update.message.reply_text(
            "🤖 I didn’t recognize that input.\n"
            "Try something like:\n"
            "- dispatch SBI\n"
            "- backtest RVNL\n"
            "- Nifty 24500 CE\n"
            "- pharma"
        )

def button_handler(update, context):
    query = update.callback_query
    query.answer()
    selection = query.data
    query.edit_message_text(text=f"🧠 Running strategist module: {selection}")
    result = parse_input(selection)
    push_dispatch(USER_ID, result(selection), TOKEN)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_input))
    dp.add_handler(MessageHandler(Filters.command, start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    print("✅ Strategist is live and polling...")
    updater.idle()

if __name__ == '__main__':
    main()
