from fastapi import FastAPI
from twse_crawler import upload_DB
from utils import gen_date_list
import time
import random


app = FastAPI()

@app.get("/Date_crawler")
def Date_crawler(start_date, end_date):
    date_list = gen_date_list(start_date, end_date)
    for date in date_list:
        sleep_time = random.uniform(0.5, 7.8)
        time.sleep(sleep_time)
        upload_DB(date)
    return {"Upload_status": "Success!"}



