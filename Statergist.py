import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
import configparser
import yaml
import re

from backtestengine import run_backtest
from telepush import push_dispatch
from parser_engine import parse_input

TOKEN = 'YOUR_BOT_TOKEN'
USER_ID = 'YOUR_TELEGRAM_USER_ID'
CONFIG_PATH = 'config_dispatch.yaml'

with open(CONFIG_PATH) as f:
    config = yaml.safe_load(f)

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
        push_dispatch(USER_ID, result, TOKEN)
    else:
        start(update, context)

def button_handler(update, context):
    query = update.callback_query
    query.answer()
    selection = query.data
    query.edit_message_text(text=f"🧠 Running strategist module: {selection}")
    result = parse_input(selection)
    push_dispatch(USER_ID, result, TOKEN)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_input))
    dp.add_handler(MessageHandler(Filters.command, start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
