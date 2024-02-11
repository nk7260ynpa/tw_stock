from twse_crawler import crawler_twse
import pandas as pd

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
