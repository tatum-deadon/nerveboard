"""Terminal dashboard renderer."""

from __future__ import annotations
from typing import Dict, Any, Optional
from nerveboard.analytics import Analytics


class Dashboard:
    """Terminal-based dashboard for displaying metrics.

    Renders a clean, readable dashboard in the terminal
    using box-drawing characters and color.
    """

    def __init__(self, analytics: Analytics):
        self.analytics = analytics
        self._width = 60

    def render(self) -> str:
        """Render the full dashboard."""
        commits = self.analytics.commit_stats(30)
        contributors = self.analytics.top_contributors(5)

        lines = []
        lines.append("+" + "-" * (self._width - 2) + "+")
        lines.append("|  NERVEBOARD - Monthly Summary" + " " * (self._width - 33) + "|")
        lines.append("+" + "-" * (self._width - 2) + "+")
        lines.append(f"|  Commits: {commits['total_commits']:<10} | Authors: {len(commits.get('authors', {})):<10} |")
        lines.append("+" + "-" * (self._width - 2) + "+")
        lines.append("|  Top Contributors" + " " * (self._width - 21) + "|")
        for i, c in enumerate(contributors, 1):
            line = f"|  {i}. {c['name']:<20} {c['commits']} commits"
            lines.append(line + " " * (self._width - len(line) - 1) + "|")
        lines.append("+" + "-" * (self._width - 2) + "+")
        return "\n".join(lines)

    def print(self) -> None:
        print(self.render())
