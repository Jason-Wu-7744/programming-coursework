# Assignment 03 BSM Option Price Sensitivity

[English](README.md) | [中文](README.zh-CN.md)

A course exercise calculating European call and put prices under the Black-Scholes-Merton model. `sample_03.py` contains the reusable `BSM_Model` function and the original five plotting blocks.

## Assignment tasks

- Implement non-dividend-paying European call and put pricing.
- Vary spot price, strike, volatility, risk-free rate and time to maturity one at a time.
- Plot the call and put price response while keeping the other exercise parameters fixed.

The pricing model, five sensitivity tasks and parameter ranges were prescribed in the course materials. This is an implementation of that exercise, with no claim of a new pricing method.

## Inputs and sources

No external workbook or other file is read. The script uses scalar classroom inputs and NumPy parameter grids. Prices are in currency units, volatility and the continuously compounded interest rate are decimals, and maturity is in years. The example parameters describe a non-dividend-paying 50ETF option exercise.

The original scalar-input export source is not recorded. The [SSE option contract reference](https://english.sse.com.cn/markets/derivatives/overview/50etf/) provides product context, but is not verified provenance of the exercise snapshot. No downloaded market dataset is required or redistributed.

## Run

From the `financial-engineering` directory, after installing this course’s requirements.txt:

```powershell
Set-Location assignment-03
python sample_03.py
```

The script writes five JPG sensitivity charts into the assignment directory and opens a Matplotlib window. Chinese labels assume a locally available SimHei font.

## Known issues

- The model assumes European exercise, no dividends and the fixed BSM assumptions used in class. The plots are one-variable sensitivities rather than an empirical calibration.
- `BSM_Model` does not validate positive spot, strike, volatility and maturity, and has no special handling for zero volatility or expiry. Changing the supplied ranges may create division-by-zero or logarithm errors.
- Prices are clipped to zero; that operation does not replace input validation or a check of pricing identities.
- No automated put-call-parity or benchmark tests are included. Syntax-only compilation passed during packaging; it does not validate the numerical outputs.

