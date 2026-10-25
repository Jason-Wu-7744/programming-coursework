# Assignment 06: Root finding and intertrade durations

[English](README.md) | [中文](README.zh-CN.md)

Maintained by Jason. These are student solutions to prescribed coursework tasks, not claims of original research. Requirements are paraphrased from the course assignment; handouts and reports are not redistributed.

## Requirements

Implement bisection, Newton and secant methods; estimate a q-exponential intertrade-duration model and empirical density.

## Scripts

| Script | Observed role |
| --- | --- |
| [exercise-03.py](exercise-03.py) | Secant method |
| [exercise-04.py](exercise-04.py) | Intertrade-duration likelihood estimation |
| [exercise-05.py](exercise-05.py) | Empirical duration density and fitted distribution |
| [extra/exercise-04_duration_alternative.py](extra/exercise-04_duration_alternative.py) | Alternative intertrade-duration likelihood-root version. |

Alternative/practice versions are in extra/, previous code in legacy/, and explicitly labeled AI-assisted source versions in ai-assisted/. Unmarked versions do not establish independent authorship.

## Data and inputs

Privately place authorized January 2007 transaction exports at data/intertrade_ticks/600000_2007-01-DD.txt relative to this assignment. The scripts enumerate dates and expect GB2312 comma-separated time, price, change, volumn, amount, type fields (original volumn spelling retained). The task excludes overnight/lunch gaps and zero durations; verify the implementation before interpretation.

Literal external input filenames observed in the retained source:

No other literal external input filename is present.

Raw data is not redistributed. Preserve input filenames, encoding, field order, units, dates and sheet structure expected by the source. No download URL or data redistribution license is invented.

## Run

Install dependencies from this course directory with python -m pip install -r requirements.txt. Change to assignment-06 and run a selected script, for example:

~~~text
python exercise-01.py
~~~

Keep this assignment folder as the working directory even for code inside extra/, legacy/ or ai-assisted/. Scripts use relative inputs and may generate files or plots. Plotting needs an appropriate desktop/backend and fonts. Generate local intermediate inputs before running a dependent plotting step.

## Validation and limitations

Every retained Python file passed in-memory syntax compilation only. No imports, database/network call, empirical analysis, simulation, figure or numerical answer was executed or certified.

Bracketing, zero-derivative handling and iteration limits are incomplete. Data ordering, positive-duration filtering and density bins need review. Only absolute paths were made portable; algorithms were not corrected.

Preparation changed filenames/references, privacy-sensitive strings, personal paths and connection settings only. Known numerical behavior was documented rather than silently corrected.
