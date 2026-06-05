# Norwegian cyber-insurance penetration

**Working estimate: ~38% of Norwegian businesses with employees carry cyber
insurance (2024), with a working range of 35–42%.**

There is no public primary source that states this number. SSB does not ask it,
Eurostat does not collect it, and Finans Norge does not publish cyber as a
separate line. So we estimate it, transparently, by triangulating three
independent paths from public primary data and back-calculating against the
business population. The full argument is in [`METHODOLOGY.md`](METHODOLOGY.md).

## Scope and caveats (read before quoting)

- **The denominator matters.** ~38% is among businesses *with employees*
  (~207,800, SSB). Across *all* 656,500 active businesses, which include sole
  proprietors with no staff, the same volume implies ~12%. We use the
  with-employees denominator because that is the addressable market.
- **It is an estimate, not a measured count.** The working range is 35–42% for
  2024. The single data point that would collapse the uncertainty is the actual
  cyber premium and policy count from Finans Norge (see METHODOLOGY, "Next step").
- **The 2022 Nordic benchmark (38%, 10+ employees) is a cross-check, not the
  source.** It is a secondary report, used only to corroborate the triangulation.

## Files

- [`METHODOLOGY.md`](METHODOLOGY.md) — the argument, the three paths, the math, the limits.
- [`data/sources.md`](data/sources.md) — every input with its primary source.
- [`data/inputs.csv`](data/inputs.csv) — the inputs as machine-readable data.
- [`model/penetration.py`](model/penetration.py) — run it with `python3 model/penetration.py`.

## How to cite

> Zero One Security (2026). *Norwegian cyber-insurance penetration: a triangulation
> estimate.* https://github.com/zero-one-security/research/tree/main/norwegian-cyber-insurance

## Changelog

- **2026-06-05** — v1. Triangulation estimate, ~38% (businesses with employees,
  2024). Pending: replacement with measured Finans Norge premium / policy data.
