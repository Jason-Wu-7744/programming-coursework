# Focused code and documentation audit

English | [中文](AUDIT.zh-CN.md)

This follow-up audit corrects confirmed implementation errors in the public working copy. E-drive submissions were not changed, and withheld teacher-reference material was not restored. The archive remains coursework rather than an investment tool or an originality claim.

## Corrections and evidence

| Area | Before | Corrected behavior and focused check |
| --- | --- | --- |
| FNA assignment 08 Gaussian elimination, exercises 01/03 | Integer arrays truncated fractional updates. The embedded 4-by-4 example had infinity-norm residual 0.8888888888888891. | Float augmented matrices; integer, fractional and pivot-swap cases compared with numpy.linalg.solve and checked by residual. |
| FNA assignment 09, all three scripts | Difference of norms falsely stopped a triangular example at [-1,-1,1], residual 4, rather than [3,-1,1]. Gauss–Seidel returned the old iterate. | Iterate-difference and residual infinity-norm checks, latest return and finite cap. Tests cover false stopping, known solutions, invalid diagonals and divergence. |
| FNA assignment 08 primary LPPLS plot | Fitting used log(tc-t); plotting used log(t). | Both now use time to the critical date; compared at three synthetic times. Fixed nonlinear parameters and historical assumptions remain. |
| FE assignment 01 | Futures-on-portfolio slopes were used as portfolio hedge ratios. | Portfolio-on-futures fits in both selection and final-fit blocks. Synthetic slope 2.0 is recovered and agrees with covariance/variance and a local hedged-variance minimum. Actual dates/data remain unverified. |
| BDFC assignment 08 original/AI backtests | Direct zero-count log terms yielded NaN; AI coverage explicitly returned NaN for zero/all exceedances. | scipy.special.xlogy implements the zero-count limit. Tests cover zero/all, alternating and mixed events. Independence stays NaN when a predecessor state is unobserved and its transition probability is not identified. Original loss/return sign conventions remain distinct. |

The hedge direction follows the underlying-on-futures formulation in the [CFA Institute tutorial](https://www.cfainstitute.org/sites/default/files/-/media/documents/book/rf-publication/2013/rf-v2013-n3-1-pdf.pdf). Zero-count likelihoods use [SciPy's xlogy contract](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.xlogy.html), which returns zero for a zero multiplier. These support narrow fixes, not unrun historical financial results.

## Reproduce the checks

From the root with NumPy, pandas, SciPy and statsmodels installed:

~~~text
python tools/test_numerical_fixes.py
python check_coursework.py
~~~

Tests extract function definitions or selected expressions through Python AST. They never import whole course scripts, read private data, make requests or generate reports. Syntax/link checks are separate. These focused tests do not fully validate all 133 coursework files.

## Language and teaching materials

English is the documentation default, with Chinese companions and links. Quality notes, the course paper, withheld-reference explanations and supplementary notes now have Chinese companions. Assignment Chinese pages may summarize and link to detailed English notes.

Historical Chinese source comments, chart/console labels and report-generator text remain untranslated. This is not an app-language change. Slides, full prompts, raw provider exports and withheld reference/answer code remain excluded.

## Remaining limitations

No data-dependent empirical analysis was run and historical packages were not fully reconstructed. Explicit inverses, regression date/row alignment, return definitions and annualization, risk-free-rate conventions, zero-filled returns, calendars, distribution assumptions, incomplete GBM difference schemes and tail-sample filtering remain review items. No coursework license has been selected.

## Additional bounded corrections

- BDFC assignment 02: three-month winner holding returns now consistently use the winner stock; an explicit MonthEnd offset replaces the removed pandas M alias. Synthetic winner/loser and monthly-aggregation fixtures are tested.
- FE assignment 04: all eight fsolve-to-scalar assignments use item(). Tested NumPy versions issued a deprecation warning before the correction, not a TypeError. Positivity and solver-convergence limits remain.
- Four Fama–MacBeth coefficient reads now use explicit positional iloc access; a synthetic four-parameter fit checks them. Other historical data-dependent regression compatibility still needs review.

## Local results

All ten focused test groups passed on Python 3.13.5, NumPy 2.1.3, pandas 2.2.3, SciPy 1.15.3 and statsmodels 0.14.4. Separate syntax/link checks passed on Python 3.12. The month-end expression is additionally checked on pandas 3.0.1. A raw-string correction also removes the original invalid backslash-mu syntax warning without changing printed text.
