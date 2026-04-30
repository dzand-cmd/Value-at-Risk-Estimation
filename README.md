# Value-at-Risk-Estimation

## Overview

This project implements a Value-at-Risk (VaR) estimation framework in Python to quantify potential losses in a portfolio under normal market conditions. VaR is a widely used risk metric that estimates the maximum expected loss over a given time horizon at a specified confidence level.

The project uses historical market data to compute returns and estimate VaR using statistical methods, providing insight into downside risk and tail behavior.

---

## Features

* Historical market data retrieval
* Log return computation
* VaR estimation using multiple methods
* Configurable confidence levels (e.g., 95%, 99%)
* Visualization of risk thresholds
* Foundation for advanced risk modeling

---

## System Design

The workflow is structured into three main components:

* **Data Layer**: Fetches historical price data
* **Return Engine**: Computes daily log returns
* **Risk Engine**: Estimates VaR using statistical techniques

---

## Methodology

### 1. Returns Calculation

* Compute log returns:
---

### 2. VaR Estimation Methods

#### Historical VaR

* Uses empirical distribution of past returns
* VaR is the percentile of returns at the chosen confidence level

---

#### Parametric (Gaussian) VaR

* Assumes returns are normally distributed
* Uses mean and standard deviation:

---

## Example Workflow

1. Fetch historical price data
2. Compute daily log returns
3. Estimate VaR at selected confidence levels
4. Visualize returns distribution and VaR thresholds

---

## How to Run

1. Install dependencies:

   ```bash
   pip install yfinance pandas numpy matplotlib scipy
   ```

2. Run the script:

   ```bash
   python var_estimation.py
   ```

---

## Output

* Numerical VaR estimates (e.g., 95%, 99%)
* Distribution of returns with VaR cutoff points
* Visualization highlighting downside risk

---

## Why This Matters

VaR is a core tool in risk management and is widely used by financial institutions to:

* Measure potential portfolio losses
* Set risk limits
* Allocate capital

This project demonstrates how statistical methods can be used to quantify and interpret downside risk in financial markets.

---

## Limitations

* Parametric VaR assumes normal distribution of returns
* Historical VaR depends on past data and may miss extreme events
* Does not account for changing volatility regimes
* No stress testing or scenario analysis

---

## Future Improvements

* Implement Monte Carlo VaR
* Add Conditional VaR (CVaR / Expected Shortfall)
* Incorporate volatility modeling (e.g., GARCH-based VaR)
* Extend to multi-asset portfolios
* Add backtesting framework for VaR accuracy

---

## Key Takeaway

This project provides a practical framework for estimating and interpreting Value-at-Risk using both historical and parametric approaches. It highlights the strengths and limitations of common risk models and serves as a foundation for more advanced quantitative risk management techniques.
