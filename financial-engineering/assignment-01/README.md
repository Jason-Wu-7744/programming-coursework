# Assignment 01 Equity Index Futures Hedging

[English](README.md) | [中文](README.zh-CN.md)

A course exercise comparing IF, IH, IC and IM futures as hedges for an equally weighted ten-stock portfolio. `sample_01.py` is the original standalone implementation; its financial calculations are preserved, including the issue described below.

## Assignment tasks

- Compute daily logarithmic returns for stocks and four index futures series.
- Form an equally weighted portfolio and compare linear regression fits using R squared.
- Select a futures contract, estimate a hedge ratio and calculate a short futures position for a CNY 100 million exposure.
- Plot portfolio and futures returns with a scatterplot and fitted line. The script also plots daily and cumulative log returns.

These tasks and the main calculation approach came from the course assignment. The repository does not claim that they are an original research design.

## Local data contract

Place the following workbooks next to `sample_01.py`; the first sheet is read with its first row as column headers.

| File | Required columns | Meaning |
| --- | --- | --- |
| `股票.xlsx` | `日期`, `TCL科技`, `美的集团`, `五粮液`, `中国移动`, `立讯精密`, `牧原股份`, `宁德时代`, `迈瑞医疗`, `招商银行`, `三一重工` | Trading date and daily closing prices for the ten selected stocks |
| `期货.xlsx` | Exactly five columns in the order date, IF, IH, IC, IM | Trading date and daily futures settlement prices; columns are renamed by position |

The assignment window is 2024-01-01 through 2026-03-31. Supply positive numeric prices in matching, ascending trading-date order, without missing observations. The script does not join the two files by date, so the rows must already be aligned. The last futures row supplies the price used in the contract-size calculation.

The original export provider and continuous-contract roll convention were not recorded in the source. Possible external starting points are [CFFEX](https://www.cffex.com.cn/) for futures and [SSE](https://www.sse.com.cn/) or [SZSE](https://www.szse.cn/) for equities, together with an authorized data provider that documents its continuous-series construction. These links are reconstruction references, not verified provenance of the omitted workbooks. Exact historical reproduction requires the original data and roll rule; no dataset is redistributed here.

## Run

From the `financial-engineering` directory, after installing the this course’s requirements.txt and a pandas-compatible Excel reader:

```powershell
Set-Location assignment-01
python sample_01.py
```

The script prints regressions and a position size, writes three JPG charts locally and opens a Matplotlib window. Chinese fonts may need local installation.

## Known issues

- **Regression direction is reversed.** The script uses portfolio returns as X and futures returns as Y. The assignment requires portfolio returns as Y and futures returns as X, whose slope is then used as the hedge ratio. The current slope is used directly for the hedge position and also drawn against the opposite scatterplot axes. Hedge quantities and the fitted line therefore need correction and recalculation before substantive use. This historical error has been documented without rewriting the algorithm.
- The script assumes row alignment, fixed column positions and a complete price history. It has no date-join or missing-data validation.
- Selection and estimation use the same observations; there is no out-of-sample hedge evaluation or transaction-cost analysis. The displayed position quantity is fractional rather than an implemented integer-contract decision.
- Syntax-only compilation passed during packaging. Numerical correctness and end-to-end execution with market data were not verified.

中文摘要：比较四种股指期货的股票组合套保作业。原代码保留了回归方向错误，解释套保比率前必须先修正并重新计算。
