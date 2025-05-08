import yfinance as yf
import os

# 获取当前脚本所在目录，并构造 data 目录
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, '..', 'data')
os.makedirs(data_dir, exist_ok=True)

# 要下载的 ETF 列表
tickers = ['EZU', 'VGK']
start_date = '2020-01-01'

for ticker in tickers:
    # 用 Ticker.history() 拉取干净数据
    df = yf.Ticker(ticker).history(start=start_date)
    csv_path = os.path.join(data_dir, f"{ticker}.csv")
    df.to_csv(csv_path)
    print(f"Saved {ticker} data to {csv_path}")
