# Assignment 13: Numerical differentiation and stochastic simulation

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Compare forward/backward/central differences of a tabulated spectrum; estimate GBM parameters and simulate stock prices.

## Scripts

| Script | Observed role |
| --- | --- |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

The excluded spectrum workbook tabulates q and tau(q). Three excluded RESSET price exports contain date and closing price. The code filters 2015-2024 estimation data and plots a 2025 simulation and observed series. Obtain inputs privately under valid access rights.

Literal external input filenames observed in the retained source:

- 'RESSET_DRESSTK_2011_2015_1.xlsx'
- 'RESSET_DRESSTK_2016_2020_1.xlsx'
- 'RESSET_DRESSTK_2021__1.xlsx'
- 'homework13_1_1.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-13 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

The GBM source explicitly notes incomplete use of the three requested difference schemes. Drift, annualization, calendars and error interpretation need review. Randomness is unseeded; a sample path is not a forecast.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
