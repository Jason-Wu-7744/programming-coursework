# Assignment 05: Covariance estimation and portfolio allocation

[English](README.md) | [中文](README.zh-CN.md)

Compare sample, constant, factor-based, shrinkage and EWMA covariance estimates and construct portfolio weights.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [homework_05.py](homework_05.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `RESSET_IDXCSIMONRET_1.xlsx`
- `RESSET_MRESSTK_1.xlsx`
- `RESSET_THRFACDAT_MONTHLY_1.xlsx`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- These scripts retain explicit matrix inverses and original portfolio assumptions. Recheck numerical conditioning, observation alignment, constraints and out-of-sample dates.
- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.
