import telegram

def push_dispatch(chat_id, message, token):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
