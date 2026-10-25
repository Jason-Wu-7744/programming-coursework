# Financial Engineering Coursework

[English](README.md) | [中文](README.zh-CN.md)

Four undergraduate financial engineering assignments, organized by assignment. The scripts preserve the original classroom implementations and Chinese comments. They document course exercises rather than independent research.

| Assignment | Topic | Main script | External workbook required |
| --- | --- | --- | --- |
| [01](assignment-01/README.md) | Equity index futures hedging | `sample_01.py` | Yes |
| [02](assignment-02/README.md) | Treasury futures duration hedging | `sample_02.py` | Yes |
| [03](assignment-03/README.md) | BSM option price sensitivity | `sample_03.py` | No |
| [04](assignment-04/README.md) | Implied volatility smiles | `sample_04.py` | Yes |

## Environment

Install the explicitly imported third-party libraries from this directory:

```powershell
python -m pip install -r requirements.txt
```

`datetime` is part of Python's standard library. `pylab` is supplied by Matplotlib. The requirements contain no inferred version pins. Excel-based assignments also need an `.xlsx` reader; `openpyxl` is included in the requirements for pandas workbook access.

Run each script with its own assignment directory as the working directory. Several scripts call `plt.show()` and write JPG files into that directory. Chinese plot labels assume locally installed fonts such as SimHei or Microsoft YaHei.

## Scope and validation

All four distinct standalone Python source files found in the course folder are included. The two local RAR packages were inspected for source members and contain no additional standalone Python implementations. Original workbooks, reports, figures, teaching slides, report templates, archives and IDE files are excluded. Workbook schemas and data provenance limitations are documented in each assignment.

The Python files passed syntax-only compilation. This does not verify numerical results or install dependencies. Assignments 01, 02 and 04 cannot reproduce the original outputs without separately obtained workbooks. Assignment 01's regression direction was corrected in the documented audit; read its README before interpreting any hedge ratio. Initial packaging preserved financial algorithms; subsequent bounded corrections and synthetic tests are documented in the root audit.

中文摘要：本目录按四次课程作业保存课程作业实现。原始行情数据、报告和课件不随仓库发布；运行方式及已知问题见各作业说明。

## Teaching-material boundary

Teacher slides, handouts, full assignment prompts, report templates and supplied data are excluded. The assignment summaries were newly written for this archive. The `sample_*.py` filenames alone do not establish authorship, and the available slides did not provide a complete source implementation for direct matching. No claim of unaided originality is made.
