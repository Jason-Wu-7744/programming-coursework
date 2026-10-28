# Financial Numerical Analysis

[English](README.md) | [中文](README.zh-CN.md)

Python coursework covering financial data, numerical methods and Matplotlib charts.

## Assignments

| Assignment | Contents |
| --- | --- |
| [01](assignment-01/README.md) | Python data types |
| [02](assignment-02/README.md) | Control flow and functions |
| [03](assignment-03/README.md) | NumPy and financial arrays |
| [04](assignment-04/README.md) | Matplotlib and financial charts |
| [05](assignment-05/README.md) | Pandas and price simulation |
| [06](assignment-06/README.md) | Root finding and intertrade durations |
| [07](assignment-07/README.md) | Fixed points and least squares |
| [08](assignment-08/README.md) | Direct solvers and model fitting |
| [09](assignment-09/README.md) | Iterative solvers and factor regression |
| [10](assignment-10/README.md) | Polynomial interpolation |
| [11](assignment-11/README.md) | Power iteration and financial networks |
| [12](assignment-12/README.md) | Numerical integration and distributions |
| [13](assignment-13/README.md) | Finite differences and stochastic paths |
| [14](assignment-14/README.md) | Ordinary differential equations |

[Supplementary exercises](supplementary/README.md)

<!-- gallery:start -->
## Selected results

### Monte Carlo price paths

![Monte Carlo price paths](assets/figures/historical-monte-carlo-paths.jpg)

Observed prices (black) and five simulated sample paths (color).

[Assignment 05 · simulation](assignment-05/extra/exercise-06_monte_carlo_alternative.py)

### Intraday price and volume

![Intraday price and volume](assets/figures/intraday-price-volume.jpg)

Transaction prices and volume by trading session, with the previous close marked in red.

[Assignment 04 · financial charts](assignment-04/exercise-05.py)

### Finite-difference comparison

![Finite-difference comparison](assets/figures/finite-difference-spectrum.jpg)

Forward, backward and central differences. Horizontal: α = dτ(q)/dq; vertical: f(α) = qα − τ(q).

[Assignment 13 · finite differences](assignment-13/exercise-01.py)

<!-- gallery:end -->
