# Mean Reversion Strategy on European ETFs

![Python](https://img.shields.io/badge/python-3.11-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![HTML Report](https://img.shields.io/badge/report-HTML-orange)

**Author:** Yi Zuo
**Date:** 2025-05-08

---

## Overview

This repository presents a complete Python-based mean-reversion backtest framework on two European ETF symbols (EZU and VGK). It covers:

* **Data acquisition**: Automatic download of historical price data via `yfinance`.
* **Strategy implementation**: Simple mean-reversion using 30-day SMA signals.
* **Transaction cost modeling**: 0.1% commission per trade.
* **Performance metrics**: Annualized Sharpe Ratio and Maximum Drawdown.
* **Reporting**: Automated generation of HTML and PDF analysis reports.

The project is designed to be a template for quant strategy research and portfolio construction.

---

## Repository Structure

```
mean_reversion_strategy/
├─ src/                       # Source code
│  ├─ download_data.py        # Download ETF data
│  ├─ mean_reversion_backtest.py  # Single-ETF backtest
│  ├─ multi_backtest.py       # Multi-ETF comparison
│  └─ metrics.py              # Sharpe & max-drawdown calculations
├─ notebooks/                 # Jupyter analysis reports
│  ├─ mean_reversion_analysis.ipynb
│  ├─ mean_reversion_analysis.html
│  └─ mean_reversion_analysis.pdf
├─ output/                    # Generated output images
│  └─ mean_reversion_plot.png
├─ .github/                   # GitHub Actions workflows
│  └─ workflows/ci.yml
├─ .gitignore
├─ requirements.txt           # Python dependencies
└─ README.md                  # Project overview and instructions
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone git@github.com:zuoyi666/mean_reversion_strategy.git
cd mean_reversion_strategy

# 2. Create and activate Conda environment
conda create -n quant python=3.11 -y
conda activate quant

# 3. Install dependencies
pip install -r requirements.txt
playwright install

# 4. Download data and run backtests
python src/download_data.py
python src/mean_reversion_backtest.py

# 5. Generate analysis report
jupyter nbconvert --execute --to html notebooks/mean_reversion_analysis.ipynb
open notebooks/mean_reversion_analysis.html
```

---

## Performance Metrics

| Metric       | EZU         | VGK         |
| ------------ | ----------- | ----------- |
| Sharpe Ratio | \<computed> | \<computed> |
| Max Drawdown | \<computed> | \<computed> |

*Replace `<computed>` with actual values from your notebook output.*

---

## Continuous Integration

A GitHub Actions workflow (`.github/workflows/ci.yml`) is included to automatically:

1. Install dependencies
2. Execute backtest script
3. Run the Jupyter notebook to regenerate HTML report
4. Upload the HTML report as an artifact

You can view the CI status badge above.

---

## License

This project is licensed under the [MIT License](LICENSE).
© 2025 Yi Zuo
