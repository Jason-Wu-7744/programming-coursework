# Assignment 10: Polynomial interpolation

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Implement Lagrange interpolation, Newton divided differences, error illustrations and an installment-interest example.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Nodal-product illustrations |
| [exercise-04.py](exercise-04.py) | Newton divided differences |
| [exercise-05.py](exercise-05.py) | Installment rate by roots and interpolation |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Small tabulations and installment constants are embedded course inputs; no external file is required. The installment example is a fixed historical problem rather than a current lending offer.

Literal external input filenames observed in the retained source:

No other literal external input filename is present.

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-10 and run a selected script, for example:

~~~text
python exercise-03.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Grids, cash-flow convention, error estimates and extrapolation behavior are unvalidated; source algorithms are retained.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.

Some classroom-reference or interpolation scripts are withheld pending source confirmation; see the repository teaching-material boundary.
