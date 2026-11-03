#!/usr/bin/env python3
"""
REST API & Full-Stack Command Center for Rick and Morty Character Data
Includes: Instant In-Memory + CSV Cache, /healthcheck, Prometheus /metrics, and Citadel UI
"""

from collections import Counter
import csv
import io
import json
from pathlib import Path
import time
from typing import Dict, List

from flask import Flask, Response, jsonify, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
import requests

BASE_DIR = Path(__file__).resolve().parent
CACHE_JSON_PATH = BASE_DIR / "characters_cache.json"
CSV_PATH = BASE_DIR / "output.csv"
START_TIME = time.time()

app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Rick and Morty API", version="2.0.0")

API_BASE_URL = "https://rickandmortyapi.com/api/character?species=Human&status=Alive"

_MEMORY_CACHE: List[Dict] = []
_CACHE_SOURCE: str = "UNINITIALIZED"


def fetch_from_upstream() -> List[Dict]:
    """Fetch and filter Human + Alive + Earth-origin characters using server-side query filter."""
    session = requests.Session()
    url = API_BASE_URL
    filtered: List[Dict] = []

    while url:
        response = session.get(url, timeout=10)
        if response.status_code == 429:
            wait_sec = int(response.headers.get("Retry-After", 3))
            time.sleep(wait_sec)
            continue
        response.raise_for_status()
        data = response.json()

        for char in data.get("results", []):
            origin_name = char.get("origin", {}).get("name", "")
            if (
                char.get("species") == "Human"
                and char.get("status") == "Alive"
                and origin_name.startswith("Earth")
            ):
                filtered.append(
                    {
                        "id": char.get("id"),
                        "name": char.get("name"),
                        "Name": char.get("name"),
                        "status": char.get("status"),
                        "species": char.get("species"),
                        "type": char.get("type") or "Standard Human",
                        "gender": char.get("gender", "Unknown"),
                        "origin": origin_name,
                        "location": char.get("location", {}).get("name", ""),
                        "Location": char.get("location", {}).get("name", ""),
                        "image": char.get("image", ""),
                        "Image": char.get("image", ""),
                        "episodes": len(char.get("episode", [])),
                        "created": str(char.get("created", ""))[:10],
                    }
                )
        url = data.get("info", {}).get("next")

    return filtered


def load_characters() -> List[Dict]:
    """Return cached characters in sub-millisecond time, loading from disk or upstream once."""
    global _MEMORY_CACHE, _CACHE_SOURCE
    if _MEMORY_CACHE:
        return _MEMORY_CACHE

    if CACHE_JSON_PATH.exists():
        payload = json.loads(CACHE_JSON_PATH.read_text(encoding="utf-8"))
        _MEMORY_CACHE = payload.get("characters", [])
        _CACHE_SOURCE = "IN-MEMORY (PREWARMED JSON+CSV)"
        return _MEMORY_CACHE

    if CSV_PATH.exists():
        with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        _MEMORY_CACHE = [
            {
                "id": idx + 1,
                "name": r.get("Name", ""),
                "Name": r.get("Name", ""),
                "status": "Alive",
                "species": "Human",
                "type": "Standard Human",
                "gender": "Human",
                "origin": "Earth",
                "location": r.get("Location", ""),
                "Location": r.get("Location", ""),
                "image": r.get("Image", ""),
                "Image": r.get("Image", ""),
                "episodes": 1,
            }
            for idx, r in enumerate(rows)
        ]
        _CACHE_SOURCE = "IN-MEMORY (CSV CACHE)"
        return _MEMORY_CACHE

    _MEMORY_CACHE = fetch_from_upstream()
    _CACHE_SOURCE = "IN-MEMORY (LIVE API FETCH)"
    return _MEMORY_CACHE


def build_stats(characters: List[Dict], latency_ms: float) -> Dict:
    """Compute live dimensional and location breakdown statistics."""
    dim_counts = Counter(c.get("origin") or "Earth" for c in characters)
    loc_counts = Counter(c.get("location") or c.get("Location") or "Unknown" for c in characters)
    uptime_sec = int(time.time() - START_TIME)
    mins, secs = divmod(uptime_sec, 60)
    hours, mins = divmod(mins, 60)

    return {
        "status": "healthy",
        "service": "rick-and-morty-api",
        "source": _CACHE_SOURCE,
        "cache_latency_ms": round(latency_ms, 2),
        "uptime_seconds": uptime_sec,
        "uptime_human": f"{hours:02d}:{mins:02d}:{secs:02d}",
        "total_characters": len(characters),
        "dimensions_count": len(dim_counts),
        "locations_count": len(loc_counts),
        "dimensions": dict(dim_counts.most_common()),
        "locations": dict(loc_counts.most_common()),
    }


@app.route("/healthcheck", methods=["GET"])
@app.route("/health", methods=["GET"])
def healthcheck():
    """Health check endpoint for Kubernetes Liveness & Readiness Probes."""
    return jsonify({"status": "healthy", "service": "rick-and-morty-api"}), 200


@app.route("/characters", methods=["GET"])
def get_characters():
    """Get all filtered characters (Human, Alive, Earth Origin)."""
    try:
        characters = load_characters()
        return jsonify({"count": len(characters), "characters": characters}), 200
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/stats", methods=["GET"])
def api_stats():
    """Return live SRE telemetry and multiverse analytics."""
    t0 = time.perf_counter()
    characters = load_characters()
    elapsed_ms = (time.perf_counter() - t0) * 1000
    return jsonify(build_stats(characters, elapsed_ms)), 200


@app.route("/api/export.csv", methods=["GET"])
def export_csv():
    """Download filtered characters as CSV."""
    characters = load_characters()
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=["Name", "Location", "Image"])
    writer.writeheader()
    for c in characters:
        writer.writerow(
            {
                "Name": c.get("name") or c.get("Name", ""),
                "Location": c.get("location") or c.get("Location", ""),
                "Image": c.get("image") or c.get("Image", ""),
            }
        )
    return Response(
        buf.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=characters.csv"},
    )


@app.route("/", methods=["GET"])
def index():
    """Render Full-Stack Citadel Command Center UI or JSON API overview."""
    if request.args.get("format") == "json":
        return (
            jsonify(
                {
                    "service": "Rick and Morty Character API",
                    "endpoints": {
                        "/": "GET - Full-Stack Citadel Command Center UI",
                        "/characters": "GET - Fetch all Human, Alive characters from Earth",
                        "/api/stats": "GET - Live SRE & Multiverse analytics",
                        "/api/export.csv": "GET - Download CSV artifact",
                        "/healthcheck": "GET - Health check endpoint",
                        "/health": "GET - Health check endpoint (alias)",
                        "/metrics": "GET - Prometheus metrics stream",
                    },
                }
            ),
            200,
        )

    t0 = time.perf_counter()
    characters = load_characters()
    elapsed_ms = (time.perf_counter() - t0) * 1000
    stats = build_stats(characters, elapsed_ms)
    return render_template(
        "index.html",
        stats=stats,
        characters_json=json.dumps(characters, ensure_ascii=False),
    )


if __name__ == "__main__":
    load_characters()
    app.run(host="0.0.0.0", port=5000, debug=False)
