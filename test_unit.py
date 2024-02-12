from twse_crawler import crawler_twse
import pandas as pd
from utils import gen_date_list

def test_holiday_crawler():
    date = "2024-01-01"
    df = crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_weekend_crawler():
    date = "2024-01-13"
    df = crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_week_crawler():
    date = "2024-01-12"
    df = crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_en_date_list():
    start_date = "2024-01-30"
    end_date = "2024-02-02"
    date_list = gen_date_list(start_date, end_date)
    assert date_list == ["2024-01-30", "2024-01-31", "2024-02-01"]
    
