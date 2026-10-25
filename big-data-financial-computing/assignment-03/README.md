# Assignment 03: Fama–French and cross-sectional tests

[English](README.md) | [中文](README.zh-CN.md)

Combine industry time-series regressions, size/value portfolio sorting and monthly Fama–MacBeth regressions.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [fama-macbeth/homework_03_FM.py](fama-macbeth/homework_03_FM.py)
- [sort/homework_03_sort.py](sort/homework_03_sort.py)
- [timeseries/homework_03_timeseries.py](timeseries/homework_03_timeseries.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `RESSET_MRESSTK_1.csv`
- `data.csv`
- `data_matrix.csv`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- Portfolio sorting and Fama–MacBeth are specified course tasks. Recheck sorting dates, lagged information and inference before treating the estimates as a research result.
- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.
