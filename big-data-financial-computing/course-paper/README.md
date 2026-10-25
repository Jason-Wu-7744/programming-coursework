# Course paper: AI-related stocks and asset pricing

An exploratory course study combining CAPM, Fama–French regressions, joint tests, industry-chain grouping and random-forest feature importance. The course required a research topic combining financial computation and machine learning; this folder preserves the submitted code, not a peer-reviewed research claim.

## Files and execution

- `data_v1.py`: factor-data merge, regressions, joint tests and exploratory random forests.
- `pie_ML.py`: visualization code; some figures may use manually entered historical results. They are not automatically recomputed estimates.

Run scripts from this directory after supplying the data they read (`data_CN_v4.csv`, factor workbooks and subsequent derived files). Inspect each `read_csv` / `read_excel` call and column selection. Original provider data and the identifying submission documents are not redistributed.

## Interpretation and limitations

The observed model fits and importance values are exploratory associations. The retained random-forest code fits the full available sample; it does not establish out-of-sample predictive performance or causal effects. Feature importance does not by itself establish a valuation bubble. Reconcile the original report, corrected result tables and recomputed estimates before publishing quantitative conclusions.

AI-assisted alternatives and external sources should be identified as such. This archive makes no new performance, causal or investment claim.
