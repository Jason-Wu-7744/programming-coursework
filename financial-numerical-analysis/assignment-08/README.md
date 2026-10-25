# Assignment 08: Direct solvers and financial-model fitting

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Implement partial-pivot Gaussian elimination and LU; estimate a three-factor model and LPPLS linear coefficients using supplied nonlinear parameters.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Fama-French parameter estimates |
| [exercise-04.py](exercise-04.py) | LPPLS linear fit |
| [extra/exercise-04_lstsq_alternative.py](extra/exercise-04_lstsq_alternative.py) | Alternative LPPLS linear fit with numpy.linalg.lstsq. |
| [extra/lu_alternative.py](extra/lu_alternative.py) | Alternative Doolittle LU version. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

The excluded GB2312 factor-model CSV is read as Date, rm, port1, port2, port3, port4, port5, rf, SMB, HML. The excluded LPPLS CSV is read as time, close. Obtain both authorized course inputs. LPPLS tc, m and omega are supplied by the assignment; only A, B, C1 and C2 are estimated.

Literal external input filenames observed in the retained source:

- 'Exp08-Python-实验数据-LPPLS模型估参.csv'
- 'Exp08-Python-实验数据-因子模型估参.csv'

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-08 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Gaussian elimination now converts its augmented matrix to floating point, and the primary LPPLS plot now uses log(tc-t), matching its fitted design. These audit corrections have synthetic checks; explicit inverses and normal equations can still be unstable. The extra least-squares variant is not full nonlinear calibration.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
