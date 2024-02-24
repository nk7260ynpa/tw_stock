import pandas as pd
import utils
import twse_crawler 

def test_holiday_crawler():
    date = "2024-01-01"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_weekend_crawler():
    date = "2024-01-13"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_week_crawler():
    date = "2024-01-12"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_en_date_list():
    start_date = "2024-01-30"
    end_date = "2024-02-02"
    date_list = utils.gen_date_list(start_date, end_date)
    assert date_list == ["2024-01-30", "2024-01-31", "2024-02-01"]