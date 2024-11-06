"""Tests for Dashboard."""

import pytest
from nerveboard.analytics import Analytics
from nerveboard.dashboard import Dashboard


def test_dashboard_render():
    analytics = Analytics("/tmp")
    dashboard = Dashboard(analytics)
    output = dashboard.render()
    assert "NERVEBOARD" in output
