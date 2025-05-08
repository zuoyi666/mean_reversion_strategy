import pandas as pd
import matplotlib.pyplot as plt
import os

tickers = ['EZU', 'VGK']
results = {}

for ticker in tickers:
    path = os.path.join(os.path.dirname(__file__), '..', 'data', f"{ticker}.csv")
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df['SMA30'] = df['Close'].rolling(30).mean()
    df['Signal'] = 0
    df.loc[df['Close'] < df['SMA30'] - 1.5, 'Signal'] = 1
    df.loc[df['Close'] > df['SMA30'] + 1.5, 'Signal'] = -1
    df['Position'] = df['Signal'].shift(1).fillna(0)
    df['Market Return'] = df['Close'].pct_change().fillna(0)
    df['Raw Strategy Return'] = df['Position'] * df['Market Return']
    df['Trade'] = df['Position'].diff().abs()
    df['Cost'] = df['Trade'] * 0.001
    df['Strategy Return'] = df['Raw Strategy Return'] - df['Cost']
    df['Strategy Equity'] = (1 + df['Strategy Return']).cumprod()
    results[ticker] = df['Strategy Equity']

# 合并所有策略净值
equity_df = pd.DataFrame(results)

plt.figure(figsize=(12, 6))
for col in equity_df.columns:
    plt.plot(equity_df.index, equity_df[col], label=col)
plt.legend()
plt.title("Mean Reversion Strategy Equity Comparison")
plt.grid(True)
plt.show()
