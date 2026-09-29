# GeoLife processed caches

The `geolife_development.npz`, `geolife_validation.npz`, and
`geolife_test.npz` files are deterministic processed caches produced from the
recorded GeoLife source archive. They are not, by themselves, the effective
analysis split.

A 2026-09-29 audit found two cross-split pairs with identical 48-slot GPS
coordinate windows in the previously committed caches: development user 70
versus test user 13, and validation user 11 versus test user 88. Coarse 8x8
state-path equality is more common and is **not** sufficient evidence of a
duplicate trajectory.

All current analysis code must load GeoLife through `src.geolife`. The loader
forms effective splits in development -> validation -> test order and removes
later copies only when the full coordinate window is exactly identical. With
the audited caches this yields 23 development, 17 validation, and 65 effective
test users. Future regeneration through `src.prepare_data` applies the same
coordinate-fingerprint rule before writing NPZ files.
