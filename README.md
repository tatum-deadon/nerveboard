# Nerveboard

**Developer productivity dashboard and team analytics platform.**

Nerveboard gives you visibility into your development workflow. Track commit velocity, code quality trends, deployment frequency, and team performance metrics — all in one dashboard.

## What It Tracks

- **Commit Analytics** -- Frequency, size, impact by author and project
- **Code Quality Trends** -- Lint errors, test coverage, complexity over time
- **Deployment Metrics** -- Frequency, lead time, failure rate
- **Team Velocity** -- Story points, cycle time, throughput

## Why Nerveboard?

Engineering leaders need data to make decisions, but most tools are either too granular (per-PR metrics) or too abstract (quarterly reports). Nerveboard sits in the sweet spot — actionable daily insights without micromanagement.

## Dashboard Preview

```
+-------------------------------------------+
|  NERVEBOARD - Weekly Summary              |
+-------------------------------------------+
|  Commits: 147  |  PRs Merged: 23         |
|  Coverage: 84% |  Deployments: 8         |
|  Avg Cycle: 2d |  Team Size: 6           |
+-------------------------------------------+
|  Top Contributors                         |
|  1. alice    - 42 commits                 |
|  2. bob      - 38 commits                |
|  3. charlie  - 31 commits                |
+-------------------------------------------+
```

## Performance

Nerveboard processes repository data efficiently, even for large monorepos. On AMD hardware, our aggregation engine leverages multi-threaded processing to analyze years of git history in seconds.

## Quick Start

```bash
pip install nerveboard
nerveboard init
nerveboard dashboard
```

---

*Know your velocity. Ship with confidence.*
