"""Export analytics data to various formats."""

from __future__ import annotations
from typing import Any, Dict
import json
import csv
import os


class Exporter:
    """Export analytics data to JSON, CSV, or text."""

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def to_json(self, path: str) -> str:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.data, f, indent=2)
        return path

    def to_csv(self, path: str) -> str:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", newline="") as f:
            if isinstance(self.data, list) and self.data:
                writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            elif isinstance(self.data, dict):
                writer = csv.writer(f)
                for k, v in self.data.items():
                    writer.writerow([k, v])
        return path
