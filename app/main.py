#!/usr/bin/env python3
"""
Rick and Morty Character Fetcher
Fetches all Human, Alive characters from Earth and exports to CSV
"""

import requests
import csv
from typing import List, Dict

API_BASE_URL = "https://rickandmortyapi.com/api/character"


def fetch_all_characters() -> List[Dict]:
    """Fetch all characters from the API with pagination support."""
    all_characters = []
    url = API_BASE_URL
    
    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        all_characters.extend(data['results'])
        url = data['info']['next']  # None if no more pages
    
    return all_characters


def filter_characters(characters: List[Dict]) -> List[Dict]:
    """
    Filter characters by:
    - Species: Human
    - Status: Alive
    - Origin: Earth (contains 'Earth' in origin name)
    """
    filtered = []
    
    for char in characters:
        is_human = char['species'] == 'Human'
        is_alive = char['status'] == 'Alive'
        is_from_earth = 'Earth' in char['origin']['name']
        
        if is_human and is_alive and is_from_earth:
            filtered.append({
                'Name': char['name'],
                'Location': char['location']['name'],
                'Image': char['image']
            })
    
    return filtered


def write_to_csv(characters: List[Dict], filename: str = 'output.csv') -> None:
    """Write filtered characters to CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Location', 'Image'])
        writer.writeheader()
        writer.writerows(characters)
    
    print(f"Written {len(characters)} characters to {filename}")


def main():
    print("Fetching characters from Rick and Morty API...")
    
    # Fetch all characters (handles pagination)
    all_characters = fetch_all_characters()
    print(f"Total characters fetched: {len(all_characters)}")
    
    # Filter by criteria
    filtered = filter_characters(all_characters)
    print(f"Characters matching criteria: {len(filtered)}")
    
    # Write to CSV
    write_to_csv(filtered)
    
    # Print sample
    if filtered:
        print("\nSample output:")
        for char in filtered[:3]:
            print(f"  - {char['Name']}, {char['Location']}")


if __name__ == "__main__":
    main()

