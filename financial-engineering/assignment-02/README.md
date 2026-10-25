# Assignment 02 Treasury Futures Duration Hedging

[English](README.md) | [中文](README.zh-CN.md)

A course exercise using bond cash flows and duration to estimate a Treasury futures hedge. `sample_02.py` is the original standalone script, with its repeated classroom calculation blocks preserved.

## Assignment tasks

- Choose five bonds from a ten-bond exercise universe and compute accrued interest and full prices.
- Solve continuously compounded yields to maturity by bisection and calculate bond durations.
- Combine bond values and durations into portfolio measures.
- Approximate futures duration using the stated cheapest-to-deliver bond and estimate the required short futures position.

The valuation date is 2026-04-14 and the hedge horizon ends on 2026-05-14. The assignment fixes the futures contract, scalar exercise inputs and unchanged-yield/value assumptions. These are course assumptions rather than a tested market forecast or an independently designed trading strategy.

## Local data contract

Place `债券数据.xlsx` next to `sample_02.py`, with the first sheet and first row used as the table and headers.

| Column | Expected content |
| --- | --- |
| `证券简称` | Bond label |
| `到期日期` | Date parseable by pandas |
| `票面利率` | Annual coupon in percent; the script divides it by 100 |
| `每年付息次数` | Positive integer coupon frequency |
| `净价` | Clean price per CNY 100 face value |

The script selects zero-based rows 0, 1, 2, 3 and 6 from the original ten-row exercise table. Coupon dates for those specific rows and the CTD inputs are hardcoded. A replacement workbook must match those schedules, or the corresponding code inputs must be reviewed together.

The table is supplied exercise data; its market-data provider is not documented. [CFFEX](https://www.cffex.com.cn/) is an external reference for Treasury futures, and [ChinaBond](https://www.chinabond.com.cn/) provides bond-market information for an independently sourced adaptation. These are reference sources, not verified provenance of the omitted exercise rows. The workbook and teaching table are not redistributed. Scalar exercise constants already present in the source remain unchanged.

## Run

From the `financial-engineering` directory, after installing the this course’s requirements.txt and a pandas-compatible Excel reader:

```powershell
Set-Location assignment-02
python sample_02.py
```

The script prints intermediate prices, yields, durations, portfolio values and a rounded short futures quantity. It does not create a separate report file.

## Known issues

- The selected rows, coupon dates, date-count approximation, CTD choice and futures parameters are hardcoded for this exercise. Changing only the workbook can produce inconsistent calculations.
- The yield solver starts from the interval 0.01 to 0.10. It returns `None` when a sign-changing bracket is absent, and later calculations do not handle that failure.
- Coupon times use 365-day year fractions and equal fractional-year spacing. The code does not implement a general bond calendar or convention engine.
- The hedge follows the supplied fixed-CTD duration approximation and unchanged-yield/value assumptions. It does not model CTD switching, basis risk, convexity or a dynamic hedge.
- Syntax-only compilation passed during packaging. Numerical correctness and end-to-end execution with the original workbook were not verified.

中文摘要：根据债券现金流、到期收益率和久期估算国债期货套保数量。日期与选债行号固定，替换数据时需要同步复核参数。
