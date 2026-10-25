# Assignment 12: Numerical integration and distributions

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Compare composite trapezoid and Simpson rules; estimate normal weekly-return and lognormal survival probabilities.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Normal weekly-return probability |
| [exercise-04.py](exercise-04.py) | Lognormal likelihood and survival integration |
| [extra/exercise-04_scipy_alternative.py](extra/exercise-04_scipy_alternative.py) | Alternative lognormal calculation with scipy.stats. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

The excluded index-price workbook is read as date, price and resampled to weekly returns; verify historical availability and the assignment window with authorized RESSET/course access. The excluded lognormal-sample workbook is read as x.

Literal external input filenames observed in the retained source:

- 'Exp12-Python-实验数据-对数正态分布数据样本.xlsx'
- 'homework12_3_1.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-12 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Distribution assumptions, return definitions, quadrature endpoints and truncation are unvalidated. The extra scipy.stats calculation is an alternative source version rather than an independently validated benchmark.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
