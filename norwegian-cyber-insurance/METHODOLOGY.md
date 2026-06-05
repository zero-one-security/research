# Methodology: Norwegian cyber-insurance penetration

## The question

How many Norwegian businesses actually carry cyber insurance, signed and running?

## Why there is no simple answer

No open, official Norwegian source publishes this. We verified the institutions
that would hold it:

- **SSB** publishes the business population but does not ask about cyber
  insurance in its ICT-use survey.
- **Eurostat**'s "ICT security in enterprises" dataset covers security measures,
  documented routines, awareness, and incidents, but has **no cyber-insurance
  variable**.
- **Finans Norge** publishes non-life statistics but does **not** break cyber out
  as a separate line in its open tables.

The only public figure with an explicit percentage is a **secondary** benchmark
(Teknorge / NyAnalyse, *Cybersikkerhet i Norge: Nordisk benchmark 2025*), which
reports 37.98% for enterprises with 10+ employees, based on **2022** insurance
data. That report attributes the row to "Eurostat 2024", but the Eurostat dataset
contains no such variable, so the figure cannot be sourced to Eurostat. We treat
the benchmark as a cross-check only, and estimate the number ourselves from
primary data.

## The denominators

Penetration is meaningless without saying "of what". Three candidate
denominators, all from SSB (2026):

| Population | Count | Note |
|---|---|---|
| All active businesses | 656,500 | Includes sole proprietors with no staff |
| Businesses with employees | 207,800 | Our headline denominator; the addressable market |
| Enterprises with 10+ employees | smaller subset | The benchmark's scope |

We headline the **with-employees** denominator. The benchmark's 38% is scoped to
10+ employees, a smaller population, so its agreement with our figure is
corroborating, not exact. See "Limitations".

## Three independent paths

Each path estimates the annual cyber **premium pool**, which we then convert to
policies (at a weighted-average premium) and to penetration.

1. **Global share.** Global cyber premium 2024 ≈ 168 Bn NOK (Munich Re). Norway is
   ~0.48% of global GDP and more digitalised than average, so 0.5–0.8% is a
   defensible slice. At 0.6%: ≈ **1.0 Bn NOK**.
2. **Share of non-life.** Norwegian non-life premium ≈ 94.7 Bn NOK (Finans Norge,
   Q4 2024). Cyber is typically 1–3% of non-life: **0.95–2.84 Bn NOK**.
3. **Benchmark-implied.** 38% of 207,800 businesses with employees, at a 25,000
   NOK average premium ≈ **2.0 Bn NOK**.

**Convergence band: ~1.0–2.0 Bn NOK annual cyber premium.**

## From premium to penetration

At a 25,000 NOK weighted-average premium (the portfolio is bimodal: many small
5,000–15,000 policies, a few large 100,000+; 25k is a reasonable average):

| Premium pool | Policies | Penetration (with employees) | Penetration (all active) |
|---|---|---|---|
| 1.0 Bn | 40,000 | 19% | 6% |
| 1.5 Bn | 60,000 | 29% | 9% |
| **2.0 Bn** | **80,000** | **38%** | **12%** |
| 2.5 Bn | 100,000 | 48% | 15% |

## The 2024 figure

The 2022 benchmark anchors ~38% on a with-employees basis. For 2024 we apply ±4pp:

- If cyber grew with non-life (+11%): premium ≈ 2.2 Bn → ~42%.
- If cyber tracked global rate drops (−11%): premium ≈ 1.8 Bn → ~35%.

**Headline: ~38%, working range 35–42%, businesses with employees, 2024.**

## Limitations

- **Estimate, not measurement.** Built from an aggregate premium pool, not a
  counted number of policies.
- **Average-premium assumption.** The result scales inversely with the 25,000 NOK
  assumption. The sensitivity is in [`model/penetration.py`](model/penetration.py).
- **Denominator scope.** The benchmark's 38% is for 10+ employees; we apply the
  with-employees denominator (207,800). The two populations differ, so the
  apparent exact agreement is partly coincidental. Treat ~38% as a central
  estimate, not a precise measurement.
- **Data vintage.** The benchmark cross-check is 2022; the premium inputs are 2024.

## Next step: a measured number

The one data point that collapses the uncertainty is the actual Norwegian cyber
premium and policy count, held by Finans Norge member companies. Request from
Finans Norge (Kari Mørk, sjefaktuar skadeforsikring): the number of cyber policies
and unique business customers per year 2022–2024, broken down by company size.
When that lands, this estimate is replaced with a measured figure and the change
is recorded in the git history.
