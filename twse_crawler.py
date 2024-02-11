import os
import requests
import json
import pandas as pd

def zh2en_columns() -> dict[str, str]:
    zh2en_columns = {
        "證券代號": "StockID",
        "證券名稱": "StockName",
        "成交股數": "TradeVolume",
        "成交筆數": "Transaction",
        "成交金額": "TradeValue",
        "開盤價": "OpenPrice",
        "最高價": "HightestPrice",
        "最低價": "LowestPrice",
        "收盤價": "ClosePrice",
        "漲跌(+/-)": "PriceChangeSign",
        "漲跌價差": "PriceChange",
        "最後揭示買價": "FinalBuyPrice",
        "最後揭示買量": "FinalBuyVolume",
        "最後揭示賣價": "FinalSellPrice",
        "最後揭示賣量": "FinalSellVolume",
        "本益比": "PER"
    }
    return zh2en_columns

def twse_headers() -> dict[str, str]:
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'www.twse.com.tw',
        'Referer': 'https://www.twse.com.tw/zh/trading/historical/mi-index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
         }
    return headers

def html2signal() -> dict:
    html2signal = {
        "<p> </p>": " ",
        "<p style= color:green>-</p>": "-",
        "<p style= color:red>+</p>": "+",
        "<p>X</p>": "X"
    }
    return html2signal

def remove_comma(x: str) -> str:
    return x.replace(",", "")

def post_process(df: pd.DataFrame, date: str) -> pd.DataFrame:
    df = df.rename(columns=zh2en_columns())
    df["Date"] = date
    df = df[["Date"] + list(df.columns[:-1])]
    df["PriceChangeSign"] = df["PriceChangeSign"].map(html2signal())
    df["TradeVolume"] = df["TradeVolume"].map(remove_comma).astype(int)
    df["Transaction"] = df["Transaction"].map(remove_comma).astype(int)
    df["TradeValue"] = df["TradeValue"].map(remove_comma).astype(int)
    df['Date'] = pd.to_datetime(df['Date'])
    df["OpenPrice"] = df["OpenPrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["HightestPrice"] = df["HightestPrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["LowestPrice"] = df["LowestPrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["ClosePrice"] = df["ClosePrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["PriceChange"] = df["PriceChange"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["FinalBuyPrice"] = df["FinalBuyPrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["FinalBuyVolume"] = df["FinalBuyVolume"].str.replace(",", "").str.replace("--", "0").astype(int)
    df["FinalSellPrice"] = df["FinalSellPrice"].str.replace(",", "").str.replace("--", "0").astype(float)
    df["FinalSellVolume"] = df["FinalSellVolume"].str.replace(",", "").str.replace("--", "0").astype(int)
    df["PER"] = df["PER"].str.replace(",", "").astype(float)
    return df


def crawler_twse(date) -> None:
    url = f'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date.replace("-", "")}&type=ALL&response=json'
    result = requests.get(url, headers=twse_headers())
    result = result.json()
    target_table = result["tables"][8]
    df = pd.DataFrame(columns=target_table["fields"], data=target_table["data"])
    df = post_process(df, date)
    return df



