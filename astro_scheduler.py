from apscheduler.schedulers.background import BackgroundScheduler
from telepush import push_dispatch
import datetime

TOKEN = 'YOUR_BOT_TOKEN'
USER_ID = 'YOUR_TELEGRAM_USER_ID'

def daily_dispatch():
    msg = f"🌕 Daily Astro Dispatch: {datetime.date.today()}\n- Nakshatra: Rohini\n- Tithi: Shukla Paksha\n- Hora: Moon Hora till 11:00 AM"
    push_dispatch(USER_ID, msg, TOKEN)

def weekly_dispatch():
    msg = f"📅 Weekly Aspect Report: {datetime.date.today()}\n- Venus conjunct Uranus\n- Mercury ingress into Leo\n- KP: Moon sub-lord Mercury → bullish midcaps"
    push_dispatch(USER_ID, msg, TOKEN)

def monthly_dispatch():
    msg = f"🪐 Monthly Planetary Map: {datetime.date.today()}\n- Jupiter Retrograde begins\n- Saturn in Bharani\n- Combustion risk zones flagged"
    push_dispatch(USER_ID, msg, TOKEN)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_dispatch, 'cron', hour=8, minute=0)
    scheduler.add_job(weekly_dispatch, 'cron', day_of_week='fri', hour=17, minute=55)
    scheduler.add_job(monthly_dispatch, 'cron', day='last fri', hour=20, minute=55)
    scheduler.start()
