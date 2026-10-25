# Financial Numerical Analysis

[English](README.md) | [中文](README.zh-CN.md)

Python coursework archive maintained by **Jason**, organized as assignments 01-14 within the **Programming Coursework Portfolio** collection. Required exercises, alternatives, practice, an older source version and explicitly labeled AI-assisted versions are preserved. Byte-identical copies are represented once, with a link where an exercise is repeated across assignments.

These are student solutions to prescribed tasks, not claims of original research. Alternative filenames do not prove originality. Classroom-practice provenance has not been independently verified. Explicit other-person files, their unverified helper and the exam directory are excluded. Instructor handouts, reports, raw datasets, databases, generated figures and archives are not redistributed. No license to redistribute external course or financial data is asserted.

## Assignment index

| Assignment | Topic | Available Python files |
| --- | --- | ---: |
| [01](assignment-01/README.md) | Python data types | 10 |
| [02](assignment-02/README.md) | Control flow and functions | 9 |
| [03](assignment-03/README.md) | NumPy and financial arrays | 22 |
| [04](assignment-04/README.md) | Matplotlib and financial charts | 6 |
| [05](assignment-05/README.md) | Pandas and geometric Brownian motion | 12 |
| [06](assignment-06/README.md) | Root finding and intertrade durations | 6 |
| [07](assignment-07/README.md) | Fixed points and least squares | 6 |
| [08](assignment-08/README.md) | Direct solvers and financial-model fitting | 6 |
| [09](assignment-09/README.md) | Iterative solvers and three-factor regression | 3 |
| [10](assignment-10/README.md) | Polynomial interpolation | 3 |
| [11](assignment-11/README.md) | Power iteration and financial networks | 3 |
| [12](assignment-12/README.md) | Numerical integration and distributions | 5 |
| [13](assignment-13/README.md) | Numerical differentiation and stochastic simulation | 2 |
| [14](assignment-14/README.md) | Ordinary differential equations | 4 |

[Shared notes](shared/README.md) explain why the cross-week reference file is withheld. [Supplementary practice](supplementary/README.md) holds top-level exercises with unknown assignment association.

## Environment and running

~~~text
python -m pip install -r requirements.txt
~~~

Requirements reflect observed imports; source versions and a lockfile were absent, so versions are not invented. pymysql is selected by retained SQLAlchemy URLs; openpyxl supports pandas XLSX readers. akshare is used by a supplementary request. Turtle, pickle, math and os are Python standard-library modules. Runtime/package compatibility, APIs, GUI backends and requested fonts have not been tested.

Each assignment README describes requirements, script roles, input fields/source, working directory and known limitations. Run each script from its assignment directory, even when the script is in a subfolder. The shared/ page explains why the cross-week reference source is withheld.

## Private inputs and connection configuration

Obtain course tables, RESSET exports and research-derived network data through authorized access. Input filenames and observed schemas are documented; no download address is invented. Keep data private and outside version control. Small numerical tables embedded in exercise source are retained.

Database scripts require FNA_DB_HOST, FNA_DB_PORT, FNA_DB_USER, FNA_DB_PASSWORD and FNA_DB_NAME in the process environment. All must be supplied privately; no original value remains. [.env.example](.env.example) lists names only and is not automatically loaded. Do not commit populated environment files or private data.

## Validation and historical behavior

All retained Python files passed in-memory syntax compilation. This does not execute imports or establish numerical, empirical or runtime correctness. No database access, network request, simulation, estimate, chart or numerical answer was executed or certified.

Original algorithms were preserved. Publication preparation normalized filenames/references, removed personal identifiers and absolute machine paths, replaced embedded connection settings with environment reads and removed commented connection/SQL examples. Known issues remain documented in assignment READMEs: integer-array elimination, iterative stopping/return behavior, LPPLS fit/plot inconsistency, zero-filled missing returns, coverage gaps and incomplete GBM difference schemes. Some original plotting strings produce escape-sequence warnings.

A private preparation audit is stored outside this repository and must not be published. Public maintainer: Jason.

## Teaching-material boundary

Teacher slides, handouts, full assignment prompts, supplied answer code and source datasets are not redistributed. The brief task summaries here were written for this archive.

Source files that matched a classroom example or whose classroom-reference provenance remained unresolved have been withheld pending authorship confirmation or permission. This is a conservative publication choice, not a determination of copyright ownership or proof of copying. Assignment folders remain available even when some reference-dependent scripts are withheld.
