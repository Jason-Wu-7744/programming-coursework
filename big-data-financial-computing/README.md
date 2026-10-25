# Big Data and Financial Computing

[English](README.md) | [中文](README.zh-CN.md)

Coursework archive by Jason. Organized by assignment to show the progression from return distributions and asset-pricing tests to portfolio allocation, volatility and risk analysis.

<!-- gallery:start -->
## Selected visual outputs

Archived Matplotlib figures from the coursework folders, with original labels retained. These images were not regenerated after the code audit. Each figure links to its implementation; see the [validation notes](QUALITY.md) for scope.

### Return distributions across seven sampling horizons

![Return distributions across seven sampling horizons](assets/figures/multiscale-return-density.jpg)

Empirical return densities from 1-minute to 240-minute sampling horizons, compared on a logarithmic density axis with distinct line styles and markers.

[Assignment 01 · return distributions](assignment-01/homework_01.py)

### Factor-model industry portfolio weights

![Factor-model industry portfolio weights](assets/figures/factor-model-industry-weights.jpg)

Changing industry allocations from factor-based covariance estimates over 2018–2021. Negative weights represent short exposures in this unconstrained allocation exercise. Legend, top to bottom: information technology, utilities, healthcare, consumer discretionary, industrials, materials, consumer staples, energy, telecommunications and financials.

[Assignment 05 · covariance and allocation](assignment-05/homework_05.py)

### GARCH(1,1) simulation and conditional volatility

![GARCH(1,1) simulation and conditional volatility](assets/figures/garch-simulation-comparison.jpg)

Simulated returns (green), conditional volatility (orange) and historical index returns (blue) on an observation index. The green series is a stochastic simulation path.

[Assignment 07 · conditional volatility](assignment-07/homework_07_01.py)

<!-- gallery:end -->


| Assignment | Topic |
| --- | --- |
| [01](assignment-01/) | Return distributions |
| [02](assignment-02/) | CAPM and return patterns |
| [03](assignment-03/) | Fama–French and cross-sectional tests |
| [04](assignment-04/) | Return predictability |
| [05](assignment-05/) | Covariance estimation and portfolio allocation |
| [06](assignment-06/) | Web data collection |
| [07](assignment-07/) | Conditional volatility |
| [08](assignment-08/) | Value at Risk and backtesting |

Also included: [course paper](course-paper/), [classroom-source withholding notice](classroom-exercises/), [data-access practice](supplementary/).

## Scope

The original student code and distinctly labeled alternatives are retained. Course tasks are not presented as original research; the AI-assisted VaR variant is explicitly labeled. Instructor-supplied sample folders, exam materials, raw database exports, original identifying reports, IDE files and caches are excluded. Selected historical chart outputs are included above with implementation links. Identical code duplicates within one assignment are represented once.

## Setup

Python 3.12 is used for publication-time syntax checks. Install the packages in `requirements.txt` in an isolated environment, read the assignment's data notes, and run a script from its own directory. Dependency versions were not fully reconstructed from the historical course environment. Most scripts use external data and are not self-contained demos.

## Validation and known issues

See [QUALITY.md](QUALITY.md). Syntax checks do not run the coursework or validate statistical conclusions. Numerical corrections are explicitly documented in the root audit: method and interpretation issues are described in the assignment notes. Original data should be independently obtained under the provider's access and redistribution conditions.

Public files use the preferred name Jason. No real API key, deployment login or student identifier should be committed. No open-source license has been selected; public availability alone is not a license grant.

## Teaching-material boundary

Teacher slides, handouts, full assignment prompts, supplied answer code and source datasets are not redistributed. The brief task summaries here were written for this archive.

Source files that matched a classroom example or whose classroom-reference provenance remained unresolved have been withheld pending authorship confirmation or permission. This is a conservative publication choice, not a determination of copyright ownership or proof of copying. Assignment folders remain available even when some reference-dependent scripts are withheld.
