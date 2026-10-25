# Assignment 09: Iterative solvers and three-factor regression

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Implement Jacobi and Gauss-Seidel and estimate sector-index three-factor models.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Sector-index Fama-French estimates |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

The excluded factor workbook is read as date, RMRF, SMB, HML. Three sector workbooks contain date and medicine/energy/materials series, renamed med/eng/mat. The task specifies RESSET monthly sector-index and three-factor data. Confirm response definition, excess returns, dates, frequency and units when obtaining authorized data.

Literal external input filenames observed in the retained source:

- '2015_2024_三因子.xlsx'
- '2015_2024_上证医药.xlsx'
- '2015_2024_上证材料.xlsx'
- '2015_2024_上证能源.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-09 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

The audit corrected the iterate-difference/residual stopping rule, latest-iterate return and finite iteration cap. Arbitrary input matrices can still fail to converge. Sector data is concatenated by row rather than joined by date. Results are unvalidated.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
