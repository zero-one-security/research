# What Norwegian cyber incidents cost

**Three figures from the public record for what a serious Norwegian cyber
incident can cost: a NOK 2 million regulatory fine (Storting), a reported
~NOK 49.7 million incident (AKVA group), and reported total costs of around
NOK 800 million (Norsk Hydro).**

These are the figures behind the "selected Norwegian cyber consequences" chart on
our site and the cases in the magazine. They are directly cited public figures,
not an estimate, so this study is a ledger: each figure, what it is, its primary
source, and the limits on what it supports.

## The figures

| Case | Figure | What it is | Year |
|---|---|---|---|
| Stortinget (national parliament) | NOK 2 million | A regulatory **fine** from Datatilsynet, not an incident cost | 2022 |
| AKVA group | ~NOK 49.7 million | Reported **total incident cost** | 2021 |
| Norsk Hydro | ~NOK 800 million | Company-reported **total cost** of the 2019 attack | 2019 |

## Scope and caveats (read before quoting)

- **The Storting figure is a fine, not a loss.** Datatilsynet's 2022 decision
  imposed a NOK 2 million administrative fine, and was explicit that the Storting
  "did not have two-factor authentication or equivalent effective security
  measures." It belongs on a magnitude chart only as a regulatory consequence,
  not as an incident cost comparable to the other two.
- **These do not establish a cause.** In none of these cases does the public
  record cleanly show that stolen or phished credentials were the way in. The
  Hydro attack was a LockerGoga ransomware infection documented at the time, but
  its initial-access path has never been settled in public. These figures prove
  that Norwegian incidents can be very expensive. They do not prove that one
  control would have prevented them.
- **AKVA is press-reported.** The ~NOK 49.7 million figure comes from Teknisk
  Ukeblad, a trade press report, not a regulator or the company's audited filing.
- **Nordic Choice has no high-confidence loss figure.** We carry it only as a
  named example of a trusted-email entry vector (an attachment that appeared to
  come from a partner), not as a number. See [`data/sources.md`](data/sources.md).

## What these figures support

A two-step, deliberately narrow argument: serious Norwegian incidents can be very
expensive, and the insurance gap is wide (see
[`../norwegian-cyber-insurance/`](../norwegian-cyber-insurance/)), so hardening
plus insurability is rational. They do **not** claim a shared cause across the
cases, that one cyber policy would have paid these losses, or that any single
control would have prevented them.

## Files

- [`data/sources.md`](data/sources.md) — every figure with its primary source and tier.
- [`data/inputs.csv`](data/inputs.csv) — the figures as machine-readable data.

## How to cite

> Zero One Security (2026). *What Norwegian cyber incidents cost: a public-record
> ledger.* https://github.com/zero-one-security/research/tree/main/norwegian-incident-costs

## Changelog

- **2026-06-10** — v1. Three public-record figures (Storting fine, AKVA, Hydro)
  plus attack-vector and attribution sources (Nordic Choice/Conti, LockerGoga).
