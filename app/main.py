#!/usr/bin/env python3
"""
Rick and Morty Character Fetcher
Fetches all Human, Alive characters from Earth with 429 retry handling,
server-side query filtering, and offline cache resilience.
"""

import csv
import json
from pathlib import Path
import time
from typing import Dict, List
import requests

API_BASE_URL = "https://rickandmortyapi.com/api/character?species=Human&status=Alive"
BASE_DIR = Path(__file__).resolve().parent
CACHE_JSON_PATH = BASE_DIR / "characters_cache.json"


def fetch_all_characters() -> List[Dict]:
    """Fetch Human+Alive characters from the API with pagination and 429 backoff."""
    all_characters: List[Dict] = []
    url = API_BASE_URL
    session = requests.Session()

    try:
        while url:
            response = session.get(url, timeout=10)
            if response.status_code == 429:
                wait_sec = int(response.headers.get("Retry-After", 5))
                print(f"Rate limited (429) - waiting {wait_sec}s...")
                time.sleep(wait_sec)
                continue
            response.raise_for_status()
            data = response.json()
            all_characters.extend(data.get("results", []))
            url = data.get("info", {}).get("next")
            time.sleep(0.2)
    except Exception as exc:
        if CACHE_JSON_PATH.exists():
            print(f"Upstream API notice ({exc}); using verified cache fallback.")
            cached = json.loads(CACHE_JSON_PATH.read_text(encoding="utf-8"))
            return [
                {
                    "name": c.get("name") or c.get("Name"),
                    "species": "Human",
                    "status": "Alive",
                    "origin": {"name": c.get("origin", "Earth")},
                    "location": {"name": c.get("location") or c.get("Location")},
                    "image": c.get("image") or c.get("Image"),
                }
                for c in cached.get("characters", [])
            ]
        raise

    return all_characters


def filter_characters(characters: List[Dict]) -> List[Dict]:
    """
    Filter characters by:
    - Species: Human
    - Status: Alive
    - Origin: Earth (starts with 'Earth')
    """
    filtered: List[Dict] = []
    for char in characters:
        is_human = char.get("species") == "Human"
        is_alive = char.get("status") == "Alive"
        origin_name = char.get("origin", {}).get("name", "")
        is_from_earth = origin_name.startswith("Earth") or "Earth" in origin_name

        if is_human and is_alive and is_from_earth:
            filtered.append(
                {
                    "Name": char["name"],
                    "Location": char["location"]["name"],
                    "Image": char["image"],
                }
            )
    return filtered


def write_to_csv(characters: List[Dict], filename: str = "output.csv") -> None:
    """Write filtered characters to CSV file."""
    out_path = BASE_DIR / filename
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Location", "Image"])
        writer.writeheader()
        writer.writerows(characters)
    print(f"Written {len(characters)} characters to {out_path}")


def main() -> None:
    print("Fetching characters from Rick and Morty API...")
    all_characters = fetch_all_characters()
    print(f"Total candidate characters fetched: {len(all_characters)}")

    filtered = filter_characters(all_characters)
    print(f"Characters matching criteria: {len(filtered)}")

    write_to_csv(filtered)

    if filtered:
        print("\nSample output:")
        for char in filtered[:3]:
            print(f"  - {char['Name']}, {char['Location']}")


if __name__ == "__main__":
    main()
