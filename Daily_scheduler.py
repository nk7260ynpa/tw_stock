from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from twse_crawler import upload_DB
import time

def daily_twse_crawler():
    """
    This function is used to crawl the daily TWSE data and upload to the database.

    Parameters:
    ----------
    None

    Returns:
    ----------
    None
    """
    upload_DB(datetime.today().strftime('%Y-%m-%d'))
    print("Daily TWSE Crawler is done at", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    

def main() -> None:
    scheduler = BackgroundScheduler(timezone="Asia/Taipei")
    scheduler.add_job(id="daily_twse_crawler",
                      func=daily_twse_crawler,
                      trigger="cron",
                      hour="14",
                      minute="00",
                      day_of_week="*"
                    )
    print("Starting Scheduler...")
    scheduler.start()

if __name__ == "__main__":
    main()
    while True:
        time.sleep(3600)
