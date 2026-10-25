# Assignment 06: Web data collection

[English](README.md) | [中文](README.zh-CN.md)

Collect financial web content or endpoint data and explore basic text/sentiment and return relationships.

This topic is part of the course assignment, not a claim of a newly invented financial method. The original implementation is retained, except for privacy redactions and file organization.

## Scripts

- [homework_06_03.py](homework_06_03.py)
- [homework_06_05.py](homework_06_05.py)
- [sina-endpoint/homeworrk_06_04.py](sina-endpoint/homeworrk_06_04.py)

## Data and working directory

The original financial-data exports are not redistributed. Historical sources include RESSET and course datasets; obtain appropriate access or supply equivalent data with the columns used by the script. API examples also require the indicated provider to remain available.

Literal input filenames found in the scripts:

- `data_1999_2003.csv`
- `data_2004_2008.csv`
- `data_2009_2013.csv`
- `data_2014_2018.csv`
- `data_guba.csv`
- `data_sina_cjwl.txt`

Create a Python 3.12 environment and install the course-level `requirements.txt`. Change into the directory containing the script and place its required files there, then run `python script-name.py`. Nested alternatives have their own working-directory assumptions. Plotting scripts may require an installed CJK font; output files are created in the working directory.

## Review notes

- Web endpoints and HTML structures may have changed. Observe the provider terms and request limits; do not publish any cookies or account credentials.
- This is a course archive. Python syntax is checked separately; the historical financial results have not been fully rerun or independently validated for publication.

The original machine-specific crawler output folder has been changed to `data/`. Create that directory under the script working directory before running the relevant crawler. Original web behavior has not been revalidated.

A crawler implementation identical to the classroom sample was withheld. The remaining scripts are not represented as teacher answer code.
