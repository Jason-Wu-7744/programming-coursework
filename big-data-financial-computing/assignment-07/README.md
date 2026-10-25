# Assignment 07: Conditional volatility

[English](README.md) | [中文](README.zh-CN.md)

Estimate ARCH, GARCH and EGARCH variants, examine distributional diagnostics and compare conditional-volatility behavior.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [homework_07_01.py](homework_07_01.py)
- [homework_07_02.py](homework_07_02.py)
- [homework_07_03.py](homework_07_03.py)
- [homework_07_04.py](homework_07_04.py)
- [stock-000858/data_000858.py](stock-000858/data_000858.py)
- [stock-600000/data_600000.py](stock-600000/data_600000.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `RESSET_DRESSTK_1990_2000_1.xlsx`
- `RESSET_DRESSTK_2001_2010_1.xlsx`
- `RESSET_DRESSTK_2011_2015_1.xlsx`
- `RESSET_DRESSTK_2016_2020_1.xlsx`
- `data_000858.csv`
- `data_600000.csv`
- `stock_data_2000_2020_v2.xlsx`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.
