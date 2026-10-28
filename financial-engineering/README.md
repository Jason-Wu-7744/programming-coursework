# Introduction to Financial Engineering

[English](README.md) | [中文](README.zh-CN.md)

Four assignments and four Python scripts covering futures hedging, option pricing and implied volatility.

## Assignments

| Assignment | Topic | Code |
| --- | --- | --- |
| [01](assignment-01/README.md) | Equity index futures hedging | [sample_01.py](assignment-01/sample_01.py) |
| [02](assignment-02/README.md) | Treasury futures duration hedging | [sample_02.py](assignment-02/sample_02.py) |
| [03](assignment-03/README.md) | BSM option price sensitivity | [sample_03.py](assignment-03/sample_03.py) |
| [04](assignment-04/README.md) | Implied volatility smiles | [sample_04.py](assignment-04/sample_04.py) |

## Visual results

### Portfolio and index futures

![Cumulative log returns of the stock basket and four index futures](assets/figures/portfolio-cumulative-log-returns.jpg)

Five cumulative log-return series compare the stock basket with IF, IH, IC and IM futures. [Code](assignment-01/sample_01.py)

### Implied volatility smile

![Call and put implied volatility across strike prices](assets/figures/implied-volatility-smile-may-2026.jpg)

BSM inversion gives call and put implied-volatility curves across strikes for the May expiry. [Code](assignment-04/sample_04.py)

### Option price sensitivity

![BSM call and put prices as the underlying spot price changes](assets/figures/bsm-option-price-vs-spot.jpg)

Call and put prices respond to the underlying spot price while the other parameters remain fixed. [Code](assignment-03/sample_03.py)
