# Assignment 04 Implied Volatility Smiles

[English](README.md) | [中文](README.zh-CN.md)

A course exercise recovering BSM implied volatility from European call and put prices. `sample_04.py` preserves the original root functions and four expiry-specific calculation blocks.

## Assignment tasks

- Read strike prices and call/put prices for four option expiry months.
- Solve the BSM pricing equation for volatility at each strike using SciPy's numerical solver.
- Plot call and put implied volatility against strike for each expiry and inspect the smile shape.

The four expiries, observation date, scalar inputs and smile analysis were prescribed by the course assignment. The script implements those tasks; it is not an independently validated volatility-surface model.

## Local data contract

Place `期权价格.xlsx` next to `sample_04.py`. It must contain these four sheets, each with its first row as headers:

| Sheet | Expiry used by the script |
| --- | --- |
| `5月到期` | 2026-05-27 |
| `6月到期` | 2026-06-24 |
| `9月到期` | 2026-09-23 |
| `12月到期` | 2026-12-23 |

Every sheet requires numeric columns `行权价`, `认购期权` and `认沽期权`: strike, call price and put price in consistent currency units. Each row must pair call and put prices for the same strike and expiry; supply rows in the desired strike order. Each expiry may have a different row count. The fixed observation date is 2026-05-06, spot is 3.100, and the continuously compounded risk-free rate is 0.0142. These are scalar exercise inputs retained in the source, not a downloaded dataset.

The source provider of the exercise workbook is not recorded. [SSE option market information](https://www.sse.com.cn/assortment/options/price/) is an external starting point for independently obtaining authorized quotes and contract information. Exact reproduction requires the same historical observation snapshot, price definition and workbook structure. The referenced website is not claimed as verified provenance of the omitted workbook, and the workbook is not redistributed.

## Run

From the `financial-engineering` directory, after installing this course’s requirements.txt and a pandas-compatible Excel reader:

```powershell
Set-Location assignment-04
python sample_04.py
```

The script writes four JPG charts in the assignment directory and opens a Matplotlib window. Chinese labels assume a locally available SimHei font.

## Known issues

- `fsolve` starts at volatility 0.3 with no positive-volatility bound, price-bound validation, convergence-status check or residual check. A returned value must not automatically be treated as a valid implied volatility.
- The root functions depend on mutable global variables. Four similar blocks repeat the calculation, and some variable names retain the first expiry's suffix for later months.
- The solver returns an array which is assigned to a scalar array element; behavior and warnings may depend on the installed NumPy version.
- The exercise treats the underlying as non-dividend-paying and uses one fixed rate. The code does not verify those assumptions against market quotes.
- Syntax-only compilation passed during packaging. Solver convergence and end-to-end execution with the original workbook were not verified. The numerical algorithm has not been rewritten.

## Follow-up compatibility correction

All eight scalar implied-volatility assignments now extract the one-element fsolve result with item(). NumPy 2.1.3, 2.2.6 and 2.3.5 emit a deprecation warning for the previous array-to-scalar conversion; no TypeError was observed in these environments. The fix does not add positivity, no-arbitrage or solver-convergence checks.
