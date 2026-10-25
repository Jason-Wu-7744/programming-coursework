# Assignment 05: Pandas and geometric Brownian motion

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Practice DataFrame selection, summaries, exports, missing observations, return/volatility estimates and stock-price simulation.

## Scripts

| Script | Observed role |
| --- | --- |
| [ai-assisted/exercise-06_monte_carlo.py](ai-assisted/exercise-06_monte_carlo.py) | Explicit AI-assisted simulation and text export. |
| [ai-assisted/exercise-06_results_plot.py](ai-assisted/exercise-06_results_plot.py) | Explicit AI-assisted observed/simulated price plot. |
| [ai-assisted/exercise-06_returns_volatility.py](ai-assisted/exercise-06_returns_volatility.py) | Explicit AI-assisted annual return/volatility. |
| [exercise-03.py](exercise-03.py) | Index OHLC and distributions |
| [exercise-04.py](exercise-04.py) | Five-stock series queries |
| [exercise-05.py](exercise-05.py) | Missing-data exercises |
| [exercise-06.py](exercise-06.py) | Course stock-database query |
| [exercise-06_monte_carlo.py](exercise-06_monte_carlo.py) | Primary return/volatility, simulation and plotting version. |
| [extra/exercise-06_monte_carlo_alternative.py](extra/exercise-06_monte_carlo_alternative.py) | Alternative stock sample and Monte Carlo plot. |
| [extra/pandas_indexing_practice.py](extra/pandas_indexing_practice.py) | Additional Pandas indexing practice. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Excluded inputs contain dated fund values, index returns/turnover/OHLC, five stock closing-price series, index series with missing values, and stock-price workbooks for 000021 and 002444. Retained SQL expects authorized stock_trading_data access, including Date, Close and Stkcd. Required connection variables: FNA_DB_HOST, FNA_DB_PORT, FNA_DB_USER, FNA_DB_PASSWORD, FNA_DB_NAME. Simulation text files are generated locally; run the matching generator before the plotting step. Obtain observations from the course provider or a source whose terms permit use.

Literal external input filenames observed in the retained source:

- 'Exp05-Python-实验数据-第5题.csv'
- 'MCSimulation_Jason_000021.txt'
- 'exercise-03_1.xlsx'
- 'exercise-04_三一重工.xlsx'
- 'exercise-04_中体产业.xlsx'
- 'exercise-04_华能国际.xlsx'
- 'exercise-04_南方航空.xlsx'
- 'exercise-04_白云机场.xlsx'
- 'exercise-06_closeprice_000021.xlsx'
- 'exercise-06_monte_carlo_alternative.txt'
- 'homework5_1_1.xlsx'
- 'homework5_2_1.xlsx'
- 'price_002444.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-05 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Source versions use differing periods, joins and filling choices. Annualization, calendars and fit quality are unvalidated. Explicit AI-assisted versions are separated and do not establish independent authorship.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
