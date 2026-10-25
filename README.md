# Programming Coursework Portfolio

English | [中文](README.zh-CN.md)

Python coursework maintained by **Jason**, covering Financial Numerical Analysis, Introduction to Financial Engineering, and Big Data and Financial Computing. All **26 assignment folders** are retained, with code, known alternative versions, input requirements and limitations documented by assignment.

## Courses

| Course | Assignments | Published Python coursework files | Focus |
| --- | ---: | ---: | --- |
| [Financial Numerical Analysis](financial-numerical-analysis/README.md) | 14 | 100 | Python, scientific computing and numerical methods with financial applications |
| [Introduction to Financial Engineering](financial-engineering/README.md) | 4 | 4 | Futures hedging, BSM option pricing and implied volatility |
| [Big Data and Financial Computing](big-data-financial-computing/README.md) | 8 | 29 | Return distributions, asset pricing, portfolios, volatility and risk |
| Total | 26 | 133 | Counts exclude each course's archive checker |

Each assignment README lists its published scripts, data requirements, working directory and known issues. The tables below summarize the course topics; the assignment notes identify which implementations are available and which reference-dependent files are withheld.

## Financial Numerical Analysis

The course progresses from Python containers, NumPy, Pandas and plotting to root finding, regression, linear systems, interpolation, eigenvalues, integration, differentiation and ordinary differential equations. Financial exercises include return and volatility estimation, stock-price simulation, factor regressions and network calculations.

| Assignment | Topic | Main content |
| --- | --- | --- |
| [01](financial-numerical-analysis/assignment-01/README.md) | Python data types | Strings, containers, financial arithmetic, comparisons and serialization |
| [02](financial-numerical-analysis/assignment-02/README.md) | Control flow and functions | Conditionals, loops, enumeration and Monte Carlo expectations |
| [03](financial-numerical-analysis/assignment-03/README.md) | NumPy and financial arrays | Array operations, matrix algebra, statistics and distributions |
| [04](financial-numerical-analysis/assignment-04/README.md) | Matplotlib and financial charts | Dual axes, polar plots, intraday trades and fund reinvestment |
| [05](financial-numerical-analysis/assignment-05/README.md) | Pandas and geometric Brownian motion | Tables, missing values, return and volatility estimates, price simulation |
| [06](financial-numerical-analysis/assignment-06/README.md) | Root finding and intertrade durations | Bisection, Newton and secant methods; duration-distribution estimation |
| [07](financial-numerical-analysis/assignment-07/README.md) | Fixed points and least squares | Convergence, linear and multiple regressions, return-tail fitting |
| [08](financial-numerical-analysis/assignment-08/README.md) | Direct solvers and financial-model fitting | Gaussian elimination, LU, three-factor regression and the linear part of LPPLS |
| [09](financial-numerical-analysis/assignment-09/README.md) | Iterative solvers and three-factor regression | Jacobi, Gauss–Seidel and sector-index factor estimates |
| [10](financial-numerical-analysis/assignment-10/README.md) | Polynomial interpolation | Lagrange interpolation, Newton divided differences and installment interest |
| [11](financial-numerical-analysis/assignment-11/README.md) | Power iteration and financial networks | Dominant eigenpairs, return correlations and sector centrality |
| [12](financial-numerical-analysis/assignment-12/README.md) | Numerical integration and distributions | Composite trapezoid and Simpson rules; normal and lognormal probabilities |
| [13](financial-numerical-analysis/assignment-13/README.md) | Numerical differentiation and stochastic simulation | Forward, backward and central differences; GBM estimation and simulation |
| [14](financial-numerical-analysis/assignment-14/README.md) | Ordinary differential equations | Euler, trapezoidal and second-order Runge–Kutta methods and applications |

See also [supplementary practice](financial-numerical-analysis/supplementary/README.md) and the [shared-reference publication notes](financial-numerical-analysis/shared/README.md).

## Introduction to Financial Engineering

Four assignments apply log returns, OLS regression, bond cash flows and duration, the BSM model and numerical root finding to derivatives pricing and hedging. The original classroom calculations are retained. Assignment 01 documents a known regression-direction error that requires correction before interpreting its hedge ratio.

| Assignment | Topic | Main content |
| --- | --- | --- |
| [01](financial-engineering/assignment-01/README.md) | Equity index futures hedging | Compare four futures series, fit regressions and calculate a hedge position |
| [02](financial-engineering/assignment-02/README.md) | Treasury futures duration hedging | Accrued interest, full prices, yields, portfolio duration and a CTD approximation |
| [03](financial-engineering/assignment-03/README.md) | BSM option price sensitivity | Effects of spot, strike, volatility, interest rates and time to expiry |
| [04](financial-engineering/assignment-04/README.md) | Implied volatility smiles | Recover call and put implied volatility across four expiry months |

## Big Data and Financial Computing

The course develops return-distribution and asset-pricing exercises into forecasting tests, covariance estimation, portfolio allocation, web data collection, conditional volatility and tail-risk analysis. Methods include CAPM, Fama–French, Fama–MacBeth, ARCH/GARCH/EGARCH, VaR and backtesting.

| Assignment | Topic | Main content |
| --- | --- | --- |
| [01](big-data-financial-computing/assignment-01/README.md) | Return distributions | Sampling intervals, empirical distributions, normal fits and tail behavior |
| [02](big-data-financial-computing/assignment-02/README.md) | CAPM and return patterns | Single-asset regressions, joint tests and reversal/momentum calculations |
| [03](big-data-financial-computing/assignment-03/README.md) | Fama–French and cross-sectional tests | Industry time-series regressions, size/value sorting and Fama–MacBeth regressions |
| [04](big-data-financial-computing/assignment-04/README.md) | Return predictability | In-sample fits, out-of-sample forecasts and specification evaluation |
| [05](big-data-financial-computing/assignment-05/README.md) | Covariance estimation and portfolio allocation | Sample, constant, factor-based, shrinkage and EWMA estimates; portfolio weights |
| [06](big-data-financial-computing/assignment-06/README.md) | Web data collection | Financial web and endpoint data, sentiment and return relationships |
| [07](big-data-financial-computing/assignment-07/README.md) | Conditional volatility | ARCH, GARCH and EGARCH estimation and distributional diagnostics |
| [08](big-data-financial-computing/assignment-08/README.md) | VaR and backtesting | Normal, GARCH, historical and POT estimates; coverage and independence tests |

Additional folders contain [course-paper code](big-data-financial-computing/course-paper/README.md), [classroom-exercise publication notes](big-data-financial-computing/classroom-exercises/README.md) and [data-access practice](big-data-financial-computing/supplementary/README.md). The course paper includes exploratory asset-pricing and random-forest analysis; its interpretation limits are documented in that folder.

## Source and version scope

All assignment folders and publishable implementation variants are kept. Byte-identical duplicates are represented once, with cross-references where needed. `extra/` contains supplementary or alternative implementations, `legacy/` contains identified earlier versions, and `ai-assisted/` marks known AI-assisted versions. Each assignment explains the observed role of its files. These labels record known provenance; an unmarked filename does not establish independent authorship.

The archive records implementations of prescribed coursework. It makes no claim that assigned methods, models or financial tasks are new research. Historical algorithms and their limitations remain visible. Preparation focused on organization, privacy and connection configuration; documented calculation issues were not silently replaced with revised answers.

Instructor slides, handouts, full assignment prompts, supplied reference or answer code, original reports, exam materials, IDE files and archives are excluded. Reference implementations that overlap classroom examples or have unresolved publication provenance are withheld, with notes retained in the relevant folders. Withholding is a publication precaution, not a determination of authorship or ownership. The short topic summaries were written for this archive and do not reproduce long passages of teaching material.

## Python environment and execution

Publication checks used **Python 3.12**. Use an isolated environment and install the requirements for the course you want to inspect. The historical dependency environment was not fully reconstructed, so runtime compatibility still needs verification.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Run the following installation commands from the repository root, choosing the relevant course:

| Course | Dependency file | Installation |
| --- | --- | --- |
| Financial Numerical Analysis | [requirements.txt](financial-numerical-analysis/requirements.txt) | `python -m pip install -r financial-numerical-analysis/requirements.txt` |
| Introduction to Financial Engineering | [requirements.txt](financial-engineering/requirements.txt) | `python -m pip install -r financial-engineering/requirements.txt` |
| Big Data and Financial Computing | [requirements.txt](big-data-financial-computing/requirements.txt) | `python -m pip install -r big-data-financial-computing/requirements.txt` |

Requirements reflect libraries used by the code and required database or Excel backends; no unrecorded version pins were invented. Some scripts also need Chinese fonts, a graphical interface, an available provider API or local input files.

**The working directory matters.** Financial Numerical Analysis generally expects the containing `assignment-XX/` directory, including for scripts stored in its subfolders; follow the assignment notes. Financial Engineering expects its individual assignment directory. Big Data and Financial Computing generally expects the script's own directory; nested variants may have additional assumptions.

For example, from the repository root, the option-sensitivity assignment needs no external workbook:

```powershell
Set-Location financial-engineering/assignment-03
python sample_03.py
```

This illustrates invocation only; it is not a report of successful execution. Other assignments may require private data first, and scripts can write figures or result files into their working directory.

## External data and local configuration

Original financial datasets, RESSET and other database exports, course tables and research-derived network data are not distributed. Obtain authorized inputs independently and follow each assignment's filenames, fields, dates, encoding, units and sheet structure. Source links are references for obtaining or checking inputs, not a guarantee of reproducing the historical course snapshot. Small embedded numerical tables and exercise parameters are identified in the source and assignment notes.

Configure database access privately. Relevant Financial Numerical Analysis scripts read `FNA_DB_HOST`, `FNA_DB_PORT`, `FNA_DB_USER`, `FNA_DB_PASSWORD` and `FNA_DB_NAME` from the process environment. The [configuration example](financial-numerical-analysis/.env.example) lists variable names without original values and is not automatically loaded. Keep API credentials, personal connection details, populated environment files and private data outside version control.

## Validation and limitations

The **133 published Python coursework files passed syntax checks**, and relative documentation links were checked. These checks do not establish end-to-end execution. Dependency imports, database access, network requests, estimates, simulations and charts were not comprehensively executed; financial results, statistical conclusions and forecasting performance were not comprehensively recomputed or independently validated.

Course-specific details are recorded in:

- [Financial Numerical Analysis QUALITY.md](financial-numerical-analysis/QUALITY.md)
- [Financial Engineering QUALITY.md](financial-engineering/QUALITY.md)
- [Big Data and Financial Computing QUALITY.md](big-data-financial-computing/QUALITY.md)

Documented issues include numerical stopping and convergence behavior, data alignment and missing values, fixed-parameter and plotting inconsistencies, and the regression direction in Financial Engineering Assignment 01. Read the relevant notes, prepare the inputs and review the calculations before interpreting results. No open-source license has been selected; public visibility alone grants no unstated source or external-data redistribution rights.

Maintained by **Jason**. The financial-report analysis system is maintained as a separate project.
