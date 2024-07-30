"""Analytics engine for processing repository data."""

from __future__ import annotations
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import subprocess
import json


class Analytics:
    """Process and analyze repository data.

    Extracts metrics from git history, CI pipelines,
    and project management tools.
    """

    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        self._cache: Dict[str, Any] = {}

    def commit_stats(self, days: int = 30) -> Dict[str, Any]:
        """Get commit statistics for the last N days."""
        since = (datetime.now() - timedelta(days=days)).isoformat()
        try:
            result = subprocess.run(
                f"git log --since='{since}' --format='%an|%ae|%ad' --date=short",
                shell=True, capture_output=True, text=True, cwd=self.repo_path
            )
            lines = [l for l in result.stdout.strip().split("\n") if l]
            authors: Dict[str, int] = {}
            dates: Dict[str, int] = {}
            for line in lines:
                parts = line.split("|")
                if len(parts) >= 3:
                    author = parts[0]
                    date = parts[2]
                    authors[author] = authors.get(author, 0) + 1
                    dates[date] = dates.get(date, 0) + 1
            return {
                "total_commits": len(lines),
                "authors": authors,
                "daily_commits": dates,
                "period_days": days,
            }
        except Exception:
            return {"total_commits": 0, "authors": {}, "daily_commits": {}}

    def code_stats(self) -> Dict[str, Any]:
        """Get code statistics."""
        try:
            result = subprocess.run(
                "find . -name '*.py' -not -path './.git/*' | xargs wc -l 2>/dev/null | tail -1",
                shell=True, capture_output=True, text=True, cwd=self.repo_path
            )
            lines = result.stdout.strip().split()
            total = int(lines[0]) if lines else 0
            return {"total_lines": total, "language": "python"}
        except Exception:
            return {"total_lines": 0}

    def top_contributors(self, limit: int = 5) -> List[Dict]:
        """Get top contributors by commit count."""
        stats = self.commit_stats()
        authors = stats.get("authors", {})
        sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)
        return [{"name": name, "commits": count} for name, count in sorted_authors[:limit]]
