# Assignment 07: Fixed points and least squares

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Study fixed-point convergence and ill-conditioned roots; regress a line, stock excess returns, crowdfunding amounts and heavy-tailed returns.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Least-squares line |
| [exercise-04.py](exercise-04.py) | Stock/market excess-return regression |
| [exercise-05.py](exercise-05.py) | Crowdfunding multiple regression |
| [exercise-06.py](exercise-06.py) | Tick-return density and tail regression |
| [legacy/exercise-06_previous.py](legacy/exercise-06_previous.py) | Earlier tick-return density and tail-fit version. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Excluded inputs: least_squares_points.xlsx (xi, yi); 000300_2010_2018.xlsx (Date, Close); DR001_2010_2018.xlsx (Date, Base); the course crowdfunding workbook (Mt, Sh, Qn, Qt, Pa before source transformations); and Exp07-Python-实验数据-TickReturn.mat (return vector r). Stock-price queries require authorized database access and all five FNA_DB_* variables. Obtain course, RESSET or otherwise licensed inputs privately.

Literal external input filenames observed in the retained source:

- '000300_2010_2018.xlsx'
- 'DR001_2010_2018.xlsx'
- 'Exp07-Python-实验数据-TickReturn.mat'
- 'Exp07-Python-实验数据-轻松筹项目数据.xlsx'
- 'least_squares_points.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-07 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Exercise 02 is byte-identical to assignment 06 exercise 02 and links to that canonical file. Normal equations, risk-free-rate treatment, date alignment, histograms and tail fits are unvalidated. An earlier exercise-06 version is retained in legacy/.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
