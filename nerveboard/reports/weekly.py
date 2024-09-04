"""Weekly report generator."""

from __future__ import annotations
from typing import Dict, Any
from nerveboard.analytics import Analytics
import json


class WeeklyReport:
    """Generate weekly productivity reports."""

    def __init__(self, analytics: Analytics):
        self.analytics = analytics

    def generate(self) -> Dict[str, Any]:
        """Generate a weekly report."""
        commits = self.analytics.commit_stats(7)
        contributors = self.analytics.top_contributors(10)
        code = self.analytics.code_stats()

        return {
            "period": "last_7_days",
            "commits": commits["total_commits"],
            "contributors": contributors,
            "code_stats": code,
            "generated_at": __import__("time").time(),
        }

    def to_text(self) -> str:
        report = self.generate()
        lines = [
            "=== Weekly Report ===",
            f"Commits: {report['commits']}",
            f"Contributors: {len(report['contributors'])}",
            "",
            "Top Contributors:",
        ]
        for i, c in enumerate(report["contributors"][:5], 1):
            lines.append(f"  {i}. {c['name']}: {c['commits']} commits")
        return "\n".join(lines)

    def to_json(self) -> str:
        return json.dumps(self.generate(), indent=2)
