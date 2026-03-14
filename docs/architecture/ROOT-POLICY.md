# Root Policy

Status: active
Scope: Phase 1 information architecture

This document classifies the current top-level roots so contributors do not
have to infer which surfaces are canonical, transitional, or historical.

## Root Classification

| Root | Status | Role | Notes |
| --- | --- | --- | --- |
| `README.md` | canonical | primary front door | Explains the pathway contract and directs users to Use / Learn / Build entrypoints. |
| `apps/` | canonical | education-facing app map | App-surface language is stable here even while implementation remains elsewhere. |
| `modules/` | canonical | education-facing capability map | Module language is stable here. |
| `services/` | canonical | education-facing service map | Service language is stable here. |
| `vault/` | canonical | education-facing Markdown state | Sample household truth for the pathway model. |
| `courses/` | canonical | student-facing learning scaffold | The learning ladder starts here. |
| `docs/` | canonical | reference and architecture docs | Maintainer and operator reference root. |
| `config/` | canonical | checked-in config lane | Transitional in content, but canonical as the target home for tracked config. |
| `scripts/` | canonical | checked-in operational scripts lane | Transitional in content, but canonical as the target home for owned scripts. |
| `tests/` | canonical | quality gates | Runtime and refactor safety checks. |
| `src/` | transitional | active implementation package | The live runtime remains here until moves sharpen ownership. |
| `examples/` | transitional | runnable and install examples | Keep active and stable; map into courses and pathway docs. |
| `library/` | transitional | runtime support manifests | Keep until a cleaner module/runtime support split is ready. |
| `defaults/` | transitional | shared workspace defaults | Remains active for compatibility with `uDOS` integration surfaces. |
| `.github/` | canonical | automation and CI surface | Operational governance root. |
| `.pytest_cache/` | generated | local test cache | Not a repo-facing architecture surface. |

## Policy

- New education-facing entrypoints should prefer `apps/`, `modules/`,
  `services/`, `vault/`, `courses/`, and `docs/`.
- Runtime code should continue to use `src/` until relocation clarifies, rather
  than blurs, ownership.
- `defaults/`, `examples/`, and `library/` remain valid roots during the
  transition, but they must be explicitly documented whenever surfaced.
- New generic deployment machinery should not land in `uHOME-server` if it
  belongs in `uDOS-sonic-screwdriver`.
