# Assignment 14: Ordinary differential equations

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Practice forward/backward Euler, trapezoidal and second-order Runge-Kutta on an exact-solution example, falling motion, a circuit and mortgage balances.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Trapezoid and Runge-Kutta circuit |
| [exercise-04.py](exercise-04.py) | Mortgage balance curves |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

All initial conditions, physical parameters and loan constants are embedded classroom examples. No external dataset is required.

Literal external input filenames observed in the retained source:

No other literal external input filename is present.

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-14 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Step sizes, convergence/stability, implicit updates and loan cash-flow conventions have not been independently validated.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
