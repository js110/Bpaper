# GeoLife processed caches

The `geolife_development.npz`, `geolife_validation.npz`, and
`geolife_test.npz` files are immutable processed caches produced from the
recorded GeoLife source archive. They contain the original user-ID split
candidates (23 development, 17 validation, 67 test); they are not, by
themselves, the effective analysis split.

The 2026-09-29 coordinate audit hashes the complete 48-slot float64 GPS window,
not the coarse 8x8 state path. It found these exact-coordinate duplicate
clusters in the committed caches:

- development 55 / development 75;
- development 70 / test 13;
- validation 11 / test 88;
- test 58 / test 59;
- test 69 / test 129;
- test 89 / test 144;
- test 128 / test 153 / test 163.

The effective loader processes development -> validation -> test and retains
the first member of each exact-coordinate cluster. The resulting effective
analysis split is therefore **22 development, 17 validation, and 60 test
windows**. The dropped copies are development 75 and test 13, 59, 88, 129,
144, 153, and 163.

Coarse 8x8 state-path equality is deliberately **not** a duplicate criterion:
distinct GPS paths can quantize to the same state sequence. All current
analysis code that claims decontaminated GeoLife evidence must load through
`src.geolife`. The machine-readable audit is generated as
`results/geolife_decontamination.json`.

Future regeneration through `src.prepare_data` applies the same exact
coordinate-fingerprint rule before writing NPZ files.
