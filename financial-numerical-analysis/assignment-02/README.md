# Assignment 02: Control flow and functions

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Practice loops, conditionals, functions, enumeration and a Monte Carlo expectation.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Historical classroom tax calculation |
| [exercise-04.py](exercise-04.py) | Series summation |
| [exercise-05.py](exercise-05.py) | Doubling wheat on a chessboard |
| [exercise-06.py](exercise-06.py) | Hundred-chickens enumeration |
| [exercise-07.py](exercise-07.py) | Wage-allocation enumeration |
| [exercise-08.py](exercise-08.py) | Random-door escape-time simulation |
| [extra/sine_integration_practice.py](extra/sine_integration_practice.py) | Additional fixed-grid sine integration. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

No external data is required. Numerical-integration practice in extra/ uses a fixed sine-function grid.

Literal external input filenames observed in the retained source:

No other literal external input filename is present.

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-02 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

The tax exercise retains historical classroom assumptions and has not been updated for practical payroll use. Simulations have no fixed random seed.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
