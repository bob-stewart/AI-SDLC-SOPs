# AISDLC Controls (Automation Substrate)

This folder turns SOP intent into **machine-enforceable controls**.

## What this enables

- Detect which "surfaces" a change touches (auth/network/privilege/etc)
- Require the right artifacts (evidence bundle, IRB crosscheck, approvals)
- Fail-closed on high-risk changes unless required artifacts are present
- Continuously improve the baseline through receipts → backlog → PRs

## Source of truth + lifecycle

- This repo is the **canonical baseline**.
- Downstream systems should pin the baseline by git SHA:
  - `AISDLC_BASELINE_REF=<sha>`

## Bootstrap controls

See `controls.yaml`.

Current enforcement is intentionally minimal:
- If gateable surfaces are touched, CI requires `EVIDENCE_ID=...` in the PR body.

This is the seed of the flywheel: small kernel, high leverage, continuous iteration.
