# Publication checks and interpretation

English | [中文](QUALITY.zh-CN.md)

Prepared on 25 October 2026 (Asia/Shanghai). This course archive contains 4 Python coursework files, excluding the archive checker.

## Checks

- Python 3.12 syntax-only parsing: 4 passed, 0 failed.
- Data-dependent scripts were not run. No private database or model credentials were used.
- Initial preparation organized and privacy-redacted the archive. A later audit corrected selected implementation errors with synthetic tests; see the root audit for changes and remaining limits.
- Personal identifiers, credential literals, local paths and relative documentation links are checked separately during publication preparation.
- Automated repository checks compile the source and check local README links. A green check does not establish numerical correctness, research originality or reproducibility with missing provider data.

## Running individual assignments

Read each assignment README and code before execution. Most scripts expect the original working directory, provider exports and specific column names. Obtain required data independently and verify the provider's access conditions. Install the course dependencies in a virtual environment; package versions from the original submission environment were not reconstructed or fully retested.

## Attribution and privacy

This is coursework by Jason. Assigned methods and supplied frameworks are identified as course tasks. AI-assisted or alternative versions are labeled where known. No original identifying reports, teaching slides, exam packs, raw database exports or IDE files are published. A source file being in this archive is not a claim that its financial method was invented by the student.

No open-source license has been selected. Public repository visibility alone is not a license grant.

## Focused numerical checks

Selected helper functions were tested with synthetic inputs, separately from syntax checks. No historical empirical dataset, network script or private database was run. See [the central audit](https://github.com/Jason-Wu-7744/programming-coursework/blob/main/AUDIT.md) and run python tools/test_numerical_fixes.py from the central programming-coursework repository root with the relevant numerical dependencies installed.
