# Assignment 04: Matplotlib and financial charts

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Plot standard functions, dual axes, polar curves, intraday trades and fund reinvestment.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Twin-axis sine/cosine |
| [exercise-04.py](exercise-04.py) | Polar plots |
| [exercise-05.py](exercise-05.py) | Intraday price/volume |
| [exercise-06.py](exercise-06.py) | Fund reinvestment |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

The excluded Exp04-Python-实验数据-600000_2012-12-18.txt is a GB2312 comma-separated transaction export (time, price, change, volume, turnover, trade type). Exp04-Python-实验数据-余额宝历史收益.txt is a GB2312 tab-separated date/yield series. Obtain authorized course exports and retain headers and ordering.

Literal external input filenames observed in the retained source:

- 'Exp04-Python-实验数据-600000_2012-12-18.txt'
- 'Exp04-Python-实验数据-余额宝历史收益.txt'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-04 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Logarithm domains, market-session boundaries and reinvestment assumptions have not been validated. Plotting requires a GUI backend and the fonts named by the source.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
