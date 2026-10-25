# Assignment 03: NumPy and financial arrays

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Practice array indexing, matrix algebra, statistics, probability distributions and financial tables.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Row/column deletion |
| [exercise-04.py](exercise-04.py) | Matrix rearrangement |
| [exercise-05.py](exercise-05.py) | Matrix arithmetic |
| [exercise-06.py](exercise-06.py) | Random normal array deletion |
| [exercise-07.py](exercise-07.py) | Integer filtering |
| [exercise-08.py](exercise-08.py) | Matrix identity |
| [exercise-09.py](exercise-09.py) | Transpose matrix identity |
| [exercise-10.py](exercise-10.py) | Matrix equation |
| [exercise-11.py](exercise-11.py) | Linear system |
| [exercise-12.py](exercise-12.py) | Array masking |
| [exercise-13.py](exercise-13.py) | Technology-stock arrays |
| [exercise-14.py](exercise-14.py) | Monthly-return indexing |
| [exercise-15.py](exercise-15.py) | P/E statistics |
| [exercise-16.py](exercise-16.py) | Trading amounts and logs |
| [exercise-17.py](exercise-17.py) | Bank valuation |
| [exercise-18.py](exercise-18.py) | Covariance and correlation |
| [exercise-19.py](exercise-19.py) | Portfolio and matrix decompositions |
| [exercise-20.py](exercise-20.py) | Binomial and geometric sampling |
| [exercise-21.py](exercise-21.py) | Normal and lognormal distributions |
| [exercise-22.py](exercise-22.py) | Gamma and beta distributions |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Excluded workbooks homework3_14_1.xlsx through homework3_19_1.xlsx, homework3_21_1.xlsx and homework3_22_1.xlsx contain the exercise tables: monthly returns, valuation ratios, trading amounts, bank indicators, index series, prices, and credit default/recovery samples. Preserve row/column order expected by the NumPy slices. Exercise 16 uses sheets 交易额 and 交易额变动比例; exercise 21 uses 中国石油 and 中国石化. Obtain authorized course tables privately.

Literal external input filenames observed in the retained source:

- 'exercise-14_1.xlsx'
- 'exercise-15_1.xlsx'
- 'exercise-16_1.xlsx'
- 'exercise-17_1.xlsx'
- 'exercise-18_1.xlsx'
- 'exercise-19_1.xlsx'
- 'exercise-21_1.xlsx'
- 'exercise-22_1.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-03 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Hand-written sampling tolerance conditions are not validated statistical tests. Random seeds and robust input checks are generally absent.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
