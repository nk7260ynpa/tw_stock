import pandas as pd
import utils
import twse_crawler 
import requests

def test_en_columns():
    en_columns = twse_crawler.en_columns()
    assert len(en_columns) == 16
    assert en_columns[0] == "StockID"
    assert en_columns[1] == "StockName"
    assert en_columns[2] == "TradeVolume"
    assert en_columns[3] == "Transaction"
    assert en_columns[4] == "TradeValue"
    assert en_columns[5] == "OpenPrice"
    assert en_columns[6] == "HightestPrice"
    assert en_columns[7] == "LowestPrice"
    assert en_columns[8] == "ClosePrice"
    assert en_columns[9] == "PriceChangeSign"
    assert en_columns[10] == "PriceChange"
    assert en_columns[11] == "FinalBuyPrice"
    assert en_columns[12] == "FinalBuyVolume"
    assert en_columns[13] == "FinalSellPrice"
    assert en_columns[14] == "FinalSellVolume"
    assert en_columns[15] == "PER"

def test_zh2en_columns():
    zh2en_columns = twse_crawler.zh2en_columns()
    assert len(zh2en_columns) == 16
    assert zh2en_columns["證券代號"] == "StockID"
    assert zh2en_columns["證券名稱"] == "StockName"
    assert zh2en_columns["成交股數"] == "TradeVolume"
    assert zh2en_columns["成交筆數"] == "Transaction"
    assert zh2en_columns["成交金額"] == "TradeValue"
    assert zh2en_columns["開盤價"] == "OpenPrice"
    assert zh2en_columns["最高價"] == "HightestPrice"
    assert zh2en_columns["最低價"] == "LowestPrice"
    assert zh2en_columns["收盤價"] == "ClosePrice"
    assert zh2en_columns["漲跌(+/-)"] == "PriceChangeSign"
    assert zh2en_columns["漲跌價差"] == "PriceChange"
    assert zh2en_columns["最後揭示買價"] == "FinalBuyPrice"
    assert zh2en_columns["最後揭示買量"] == "FinalBuyVolume"
    assert zh2en_columns["最後揭示賣價"] == "FinalSellPrice"
    assert zh2en_columns["最後揭示賣量"] == "FinalSellVolume"
    assert zh2en_columns["本益比"] == "PER"

def test_twse_headers():
    headers = twse_crawler.twse_headers()
    assert len(headers) == 8
    assert 'Accept' in headers
    assert 'Accept-Encoding' in headers
    assert 'Accept-Language' in headers
    assert 'Connection' in headers
    assert 'Host' in headers
    assert 'Referer' in headers
    assert 'User-Agent' in headers
    assert 'X-Requested-With' in headers

def test_html2signal():
    html2signal = twse_crawler.html2signal()
    assert " " in html2signal.values()
    assert "-" in html2signal.values()
    assert "+" in html2signal.values()
    assert "X" in html2signal.values()

def test_remove_comma():
    x = "1,000"
    x = twse_crawler.remove_comma(x)
    assert x == "1000"
    x = "1,000,000"
    x = twse_crawler.remove_comma(x)
    assert x == "1000000"

def test_post_process():
    date = '2021-10-01'
    df = pd.read_csv("tests/twse_crawler/test.csv")
    df["OpenPrice"] = df["OpenPrice"].astype("object")
    df["HightestPrice"] = df["HightestPrice"].astype("object")
    df["LowestPrice"] = df["LowestPrice"].astype("object")
    df["ClosePrice"] = df["ClosePrice"].astype("object")
    df["PriceChange"] = df["PriceChange"].astype("str")
    df["FinalBuyPrice"] = df["FinalBuyPrice"].astype("str")
    df["FinalBuyVolume"] = df["FinalBuyVolume"].astype("str")
    df["FinalSellPrice"] = df["FinalSellPrice"].astype("str")
    df["FinalSellVolume"] = df["FinalSellVolume"].astype("str")
    df["PER"] = df["PER"].astype("str")
    df = twse_crawler.post_process(df, date)
    assert df["OpenPrice"].dtype == float
    assert df["FinalBuyVolume"].dtype == int
    assert df["Date"].dtype == "datetime64[ns]"

def test_holiday_crawler(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"stat": "很抱歉，沒有符合條件的資料!"}
    mocker.patch('requests.get', return_value=mock_response)
    date = "2024-01-01"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_weekend_crawler(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"stat": "很抱歉，沒有符合條件的資料!"}
    mocker.patch('requests.get', return_value=mock_response)
    date = "2024-01-13"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)

def test_week_crawler(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"stat": "OK", 
                                       "tables": [0, 1, 2, 3, 4, 5 ,6, 7, {"fields": [1],
                                                                           "data": [1, 2, 3]}]}
    mocker.patch('requests.get', return_value=mock_response)
    mocker.patch('twse_crawler.post_process', return_value=pd.DataFrame())
    date = "2024-01-12"
    df = twse_crawler.crawler_twse(date)
    assert isinstance(df, pd.DataFrame)



def test_en_date_list():
    start_date = "2024-01-30"
    end_date = "2024-02-02"
    date_list = utils.gen_date_list(start_date, end_date)
    assert date_list == ["2024-01-30", "2024-01-31", "2024-02-01"]