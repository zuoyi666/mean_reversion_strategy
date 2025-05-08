import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def sharpe_ratio(returns, periods=252):
    """无风险利率假设为0"""
    mean_r = returns.mean() * periods
    std_r  = returns.std() * np.sqrt(periods)
    return mean_r / std_r

def max_drawdown(equity_curve):
    roll_max = equity_curve.cummax()
    drawdown = equity_curve / roll_max - 1
    return drawdown.min()


# 参数
commission = 0.001  # 每笔交易双边0.1%手续费
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

# 读取数据
df = pd.read_csv(os.path.join(data_dir, 'EZU.csv'),
                 index_col=0, parse_dates=True)

# 信号
df['SMA30'] = df['Close'].rolling(30).mean()
df['Signal'] = 0
df.loc[df['Close'] < df['SMA30'] - 1.5, 'Signal'] = 1
df.loc[df['Close'] > df['SMA30'] + 1.5, 'Signal'] = -1
df['Position'] = df['Signal'].shift(1).fillna(0)

# 收益
df['Market Return'] = df['Close'].pct_change().fillna(0)
df['Raw Strategy Return'] = df['Position'] * df['Market Return']
df['Trade'] = df['Position'].diff().abs()
df['Cost'] = df['Trade'] * commission
df['Strategy Return'] = df['Raw Strategy Return'] - df['Cost']

# 净值曲线
df['Strategy Equity'] = (1 + df['Strategy Return']).cumprod()
df['Market Equity']   = (1 + df['Market Return']).cumprod()

# 计算指标
sr = sharpe_ratio(df['Strategy Return'])
md = max_drawdown(df['Strategy Equity'])
print(f"Sharpe Ratio: {sr:.2f}")
print(f"Max Drawdown: {md:.2%}")

# 绘图并保存
output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(output_dir, exist_ok=True)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Strategy Equity'], label='Strategy Equity')
plt.plot(df.index, df['Market Equity'],   label='Market Equity')
plt.title('Mean Reversion Strategy vs Buy & Hold (EZU)')
plt.legend()
plt.grid(True)
# 将图保存为PNG，不再阻塞
out_path = os.path.join(output_dir, 'mean_reversion_performance.png')
plt.savefig(out_path)
print(f"Equity curve saved to {out_path}")
