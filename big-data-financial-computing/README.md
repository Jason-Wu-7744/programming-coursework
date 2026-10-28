# Big Data and Financial Computing

[简体中文](README.zh-CN.md)

Python coursework covering return distributions, asset pricing, portfolio allocation, volatility and risk analysis.

## Assignments

| Assignment | Contents |
| --- | --- |
| [01](assignment-01/README.md) | Return distributions |
| [02](assignment-02/README.md) | CAPM and return patterns |
| [03](assignment-03/README.md) | Factor models and cross-sectional tests |
| [04](assignment-04/README.md) | Return predictability |
| [05](assignment-05/README.md) | Covariance estimation and portfolio allocation |
| [06](assignment-06/README.md) | Financial web data collection |
| [07](assignment-07/README.md) | Conditional volatility |
| [08](assignment-08/README.md) | Value at Risk and backtesting |

[Course paper: AI-related stocks and asset pricing](course-paper/README.md) · [Financial-data access practice](supplementary/README.md)

## Results showcase

### Return distributions across seven sampling horizons

![Return distributions across seven sampling horizons](assets/figures/multiscale-return-density.jpg)

Empirical return densities from 1-minute to 240-minute horizons on a logarithmic density axis.

[Assignment 01 · code](assignment-01/homework_01.py)

### Factor-model industry portfolio weights

![Factor-model industry portfolio weights](assets/figures/factor-model-industry-weights.jpg)

Industry allocations over 2018–2021 from factor-based covariance estimates; negative weights represent short exposures.

[Assignment 05 · code](assignment-05/homework_05.py)

### GARCH(1,1) simulation and conditional volatility

![GARCH(1,1) simulation and conditional volatility](assets/figures/garch-simulation-comparison.jpg)

A simulated return path (green), its conditional volatility (orange) and historical index returns (blue).

[Assignment 07 · code](assignment-07/homework_07_01.py)
