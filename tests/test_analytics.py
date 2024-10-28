"""Tests for Analytics."""

import pytest
import tempfile
import os
from nerveboard.analytics import Analytics


def test_analytics_creation():
    analytics = Analytics("/tmp")
    assert analytics.repo_path == "/tmp"


def test_commit_stats_empty():
    analytics = Analytics("/tmp/nonexistent")
    stats = analytics.commit_stats(7)
    assert stats["total_commits"] == 0
