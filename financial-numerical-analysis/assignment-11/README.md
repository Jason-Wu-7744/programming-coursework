# Assignment 11: Power iteration and financial networks

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Compute dominant eigenpairs, a stock-return correlation matrix, and a sector ranking by eigenvector centrality.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Risk-network sector ranking |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Excluded stock workbooks have code, date, yield fields. The task specifies 2015-2019 daily returns; the retained script reads files labeled 2015 and 2016, so verify actual coverage. The excluded research-derived course network CSV has from_sector, to_sector, weight fields. Obtain authorized RESSET/course access and permission for use; no redistribution license is asserted.

Literal external input filenames observed in the retained source:

- 'Exp11-Python-上机数据_RankSectors.csv'
- 'homework11_2_1.xlsx'
- 'homework11_2_2.xlsx'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-11 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Missing returns are filled with zero, changing correlations. Power iteration lacks a seed, cap and residual check, and estimates the eigenvalue using a fixed component. Confirm directed-network orientation. The risk-network application is a prescribed task, not original research.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
