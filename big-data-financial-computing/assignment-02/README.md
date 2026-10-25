# Assignment 02: CAPM and return patterns

[English](README.md) | [中文](README.zh-CN.md)

Estimate single-asset CAPM regressions, joint tests and supplementary reversal/momentum calculations.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [extra/reversal-momentum.py](extra/reversal-momentum.py)
- [homework_02_03/homework_02_effect.py](homework_02_03/homework_02_effect.py)
- [homework_02_multi.py](homework_02_multi.py)
- [homework_02_one.py](homework_02_one.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `2000-2025上证综指日收益率_日度无风险利率.csv`
- `600016.xlsx`
- `600019.xlsx`
- `600276.xlsx`
- `600316.xlsx`
- `600320.xlsx`
- `data.csv`
- `data_matrix_daily.csv`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.

## Follow-up corrections

The three-month winner return now uses the winner stock in every holding month, rather than mixing loser returns into the first two months. Monthly resampling uses an explicit pandas MonthEnd offset instead of the removed M alias. Synthetic fixtures cover both changes; economic interpretation and historical data remain unverified.
