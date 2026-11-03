import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "app"))

from api import app


def test_healthcheck():
    client = app.test_client()
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_characters_endpoint():
    client = app.test_client()
    response = client.get("/characters")
    assert response.status_code == 200
    assert "count" in response.json
    assert response.json["count"] > 0
    first = response.json["characters"][0]
    assert "Name" in first and "name" in first
    assert "Location" in first and "location" in first
    assert "Image" in first and "image" in first


def test_stats_and_csv_export():
    client = app.test_client()
    stats_res = client.get("/api/stats")
    assert stats_res.status_code == 200
    assert stats_res.json["total_characters"] > 0

    csv_res = client.get("/api/export.csv")
    assert csv_res.status_code == 200
    assert "Name,Location,Image" in csv_res.get_data(as_text=True)


def test_dashboard_ui_renders():
    client = app.test_client()
    ui_res = client.get("/")
    assert ui_res.status_code == 200
    html = ui_res.get_data(as_text=True)
    assert "Rick &amp; Morty Multiverse Command Center" in html
    assert 'closedby="any"' in html
