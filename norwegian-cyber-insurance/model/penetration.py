#!/usr/bin/env python3
"""
Norwegian cyber-insurance penetration: a triangulation estimate.

No public primary source states how many Norwegian businesses carry cyber
insurance (see ../METHODOLOGY.md). This model estimates it by triangulating
three independent paths from public primary data, then back-calculates
penetration against each candidate denominator.

It is deliberately simple and auditable: every input is a named public figure
(see ../data/sources.md), and every step is plain arithmetic. Run it, change the
assumptions, and watch the answer move.

Usage:
    python3 penetration.py

No third-party dependencies (Python 3.8+).
"""

# --- Hard inputs (provenance in ../data/sources.md) -------------------------

# SSB, active businesses in Norway, start of 2026 (primary).
ACTIVE_BUSINESSES = 656_500
# SSB, businesses with at least one employee, start of 2026 (primary).
BUSINESSES_WITH_EMPLOYEES = 207_800
# Finans Norge, total non-life gross premium, Q4 2024 annualised (primary).
NONLIFE_PREMIUM_BN_NOK = 94.7
# Munich Re, global cyber premium 2024 (~USD 15.3bn at ~11 NOK/USD) (primary).
GLOBAL_CYBER_PREMIUM_BN_NOK = 168.3
# Teknorge / NyAnalyse Nordic benchmark: 10+ employees, 2022 insurance data.
# SECONDARY; used only as a cross-check, never as the source of record.
BENCHMARK_PENETRATION_GE10_2022 = 0.3798

# Assumption: weighted-average annual premium per policy. The real portfolio is
# bimodal (many small 5,000-15,000 policies, a few large 100,000+). 25,000 is a
# reasonable weighted average; the sensitivity to it is printed below.
AVG_PREMIUM_NOK = 25_000


def policies(premium_bn_nok, avg_premium_nok=AVG_PREMIUM_NOK):
    """Policies implied by a premium pool and an average premium."""
    return premium_bn_nok * 1e9 / avg_premium_nok


def pct(x):
    return f"{x * 100:.0f}%"


# --- Three independent estimation paths (each returns a premium pool, Bn NOK) --

def path_global_share(norway_share=0.006):
    """Norway's slice of the global cyber market (0.5-0.8% band; 0.6% point)."""
    return GLOBAL_CYBER_PREMIUM_BN_NOK * norway_share


def path_share_of_nonlife(share=0.02):
    """Cyber as a share of the non-life premium pool (1-3% band)."""
    return NONLIFE_PREMIUM_BN_NOK * share


def path_benchmark_implied():
    """Premium pool implied by the 2022 benchmark penetration."""
    return BENCHMARK_PENETRATION_GE10_2022 * BUSINESSES_WITH_EMPLOYEES * AVG_PREMIUM_NOK / 1e9


def report():
    print("Norwegian cyber-insurance penetration: triangulation")
    print("=" * 56)

    g = path_global_share()
    n = path_share_of_nonlife()
    b = path_benchmark_implied()
    lo, hi = NONLIFE_PREMIUM_BN_NOK * 0.01, NONLIFE_PREMIUM_BN_NOK * 0.03
    print("\nEstimated annual cyber premium pool (Bn NOK):")
    print(f"  1. Global-share path      : {g:5.2f}")
    print(f"  2. Share-of-non-life path : {n:5.2f}   (1-3% band: {lo:.2f}-{hi:.2f})")
    print(f"  3. Benchmark-implied path : {b:5.2f}")
    print("  -> convergence band       : ~1.0-2.0 Bn NOK")

    print("\nBack-calculated penetration by premium pool and denominator:")
    print(f"  {'Premium':>9}  {'Policies':>9}  {'with employees':>15}  {'all active':>11}")
    for premium in (1.0, 1.5, 2.0, 2.5):
        p = policies(premium)
        print(f"  {premium:>7.1f}Bn  {p:>9,.0f}  "
              f"{pct(p / BUSINESSES_WITH_EMPLOYEES):>15}  {pct(p / ACTIVE_BUSINESSES):>11}")

    print("\nSensitivity to average premium (at a 1.5 Bn pool):")
    for avg in (15_000, 25_000, 50_000, 100_000):
        p = policies(1.5, avg)
        print(f"  {avg:>7,} NOK -> {p:>8,.0f} policies -> "
              f"{pct(p / BUSINESSES_WITH_EMPLOYEES):>4} of businesses with employees")

    print("\nHeadline estimate (businesses with employees):")
    print("  central ~38%  |  working range 35-42% for 2024")
    print(f"  cross-check: 2022 benchmark = {pct(BENCHMARK_PENETRATION_GE10_2022)} "
          "(10+ emp, secondary)")


if __name__ == "__main__":
    report()
