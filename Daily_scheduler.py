from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from twse_crawler import upload_DB
import time

def daily_twse_crawler():
    upload_DB(datetime.today().strftime('%Y-%m-%d'))
    

def main():
    scheduler = BackgroundScheduler(timezone="Asia/Taipei")
    scheduler.add_job(id="daily_twse_crawler",
                      func=daily_twse_crawler,
                      trigger="cron",
                      hour="10",
                      minute="13",
                      day_of_week="*"
                    )
    scheduler.start()

if __name__ == "__main__":
    main()
    while True:
        time.sleep(3600)
