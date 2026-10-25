# Assignment 08: Value at Risk and backtesting

[English](README.md) | [中文](README.zh-CN.md)

Estimate normal, GARCH, historical and POT tail-risk measures, then apply coverage and independence checks.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [ai-assisted/generate_report.py](ai-assisted/generate_report.py)
- [ai-assisted/homework_08.py](ai-assisted/homework_08.py)
- [homework_08.py](homework_08.py)
- [homework_08_test.py](homework_08_test.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `Data_VaR.csv`
- `Data_VaR_GARCH-t.csv`
- `shdl_raw.csv`
- `上海电力_600021_上市以来日度收盘价---7b9a77f4-7e7c-4908-9e09-571f1e2606c2.xlsx`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- The original script filters some large absolute returns. This can affect tail-risk estimates and must be reassessed before interpreting results. Check loss/return sign conventions, window sizes and boundary cases in likelihood tests.
- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.
- `ai-assisted/` preserves a separately labeled AI-assisted version; it is not represented as unaided student code.

Publication privacy changes: the report generator uses a generic Jason author block and its own directory rather than an academic identity template or a server home path. A student-number suffix was removed from the AI-assisted script description.
