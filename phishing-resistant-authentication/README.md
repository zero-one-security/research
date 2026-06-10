# Phishing-resistant authentication: the evidence base

**Three public claims behind our authentication writing: the national security
authority (NSM) recommends phishing-resistant multi-factor authentication over
weaker forms; Microsoft reports passkey sign-ins are eight times faster than a
password and MFA; and the FIDO Alliance describes BankID, used by about 4.7
million people (roughly 97% of Norway), as part of the same move to
passkey-based authentication.**

These are the cited claims behind the magazine pieces on hardware keys and the
five Norwegian cases. They are directly cited public statements, not an estimate,
so this study is a ledger: each claim, its primary source, and what it does and
does not support.

## The claims

| Claim | Source | Tier |
|---|---|---|
| NSM distinguishes phishing-resistant MFA from weaker forms and recommends the stronger category against phishing and account takeover | NSM thematic report, Flerfaktorautentisering | Primary (authority) |
| Passkey sign-ins are "eight times faster than a password and multifactor authentication" | Microsoft Security blog (2025) | Vendor-reported |
| BankID has ~4.7 million users (~97% of Norway) and is part of the passkey move | FIDO Alliance (2026) | Secondary (industry body) |

## Scope and caveats (read before quoting)

- **NSM is the authoritative recommendation.** The distinction between
  phishing-resistant MFA and weaker second factors (SMS codes, push approvals) is
  NSM's own, and the recommendation of the stronger category is theirs. This is
  the load-bearing claim; treat it as primary.
- **The Microsoft figure is vendor-reported.** "Eight times faster" is
  Microsoft's own measurement of its own sign-ins. It supports the narrow point
  that the stronger method can also be the faster one; it is not an independent
  benchmark.
- **The 4.7M / ~97% figure is FIDO's framing of BankID reach.** It describes
  population reach of BankID, cited by the FIDO Alliance in the context of the
  passkey move. It does **not** claim that 4.7 million Norwegians use FIDO
  hardware keys, only that the habit of proving identity with a possession rather
  than a recited secret is already widespread in Norway.

## What these claims support

The narrow, honest case: phishing-resistant authentication removes one important
and common class of failure (the phishing of a login), the national authority
recommends it, it need not cost the user time, and Norwegians already hold the
habit through BankID. They do **not** claim a key stops payment-redirection fraud
or malicious attachments, or that any single control removes all risk.

## Files

- [`data/sources.md`](data/sources.md) — every claim with its primary source and tier.
- [`data/inputs.csv`](data/inputs.csv) — the quantified claims as machine-readable data.

## How to cite

> Zero One Security (2026). *Phishing-resistant authentication: the evidence base.*
> https://github.com/zero-one-security/research/tree/main/phishing-resistant-authentication

## Changelog

- **2026-06-10** — v1. NSM recommendation, Microsoft passkey-speed figure, FIDO
  BankID-adoption figure.
