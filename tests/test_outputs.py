import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "Expected /app/report.json to exist"
    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json must contain valid JSON") from exc

    assert isinstance(report, dict), "The report must be a JSON object"
    return report


def test_success_criterion_1_schema():
    """Success criterion 1: verify the output path, JSON format, and exact keys."""
    report = load_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_success_criterion_2_total_requests():
    """Success criterion 2: verify the number of nonblank request lines."""
    report = load_report()
    assert type(report["total_requests"]) is int
    assert report["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """Success criterion 3: verify the number of distinct client IP addresses."""
    report = load_report()
    assert type(report["unique_ips"]) is int
    assert report["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """Success criterion 4: verify the most frequently requested path."""
    report = load_report()
    assert isinstance(report["top_path"], str)
    assert report["top_path"] == "/index.html"
