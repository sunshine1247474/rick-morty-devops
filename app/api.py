#!/usr/bin/env python3
"""
REST API Service for Rick and Morty Character Data
Bonus: Dockerized service with /healthcheck endpoint + Prometheus Metrics
"""

from flask import Flask, jsonify
import requests
from typing import List, Dict
from prometheus_flask_exporter import PrometheusMetrics
import time

app = Flask(__name__)

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Rick and Morty API', version='1.0.0')

# Custom metrics
request_latency = metrics.histogram(
    'api_request_latency_seconds',
    'Request latency in seconds',
    labels={'endpoint': lambda: 'characters'}
)

characters_fetched = metrics.counter(
    'characters_fetched_total',
    'Total number of characters fetched',
    labels={'status': lambda: 'success'}
)

API_BASE_URL = "https://rickandmortyapi.com/api/character"


def fetch_filtered_characters() -> List[Dict]:
    """Fetch and filter characters from Rick and Morty API."""
    all_characters = []
    url = API_BASE_URL
    
    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        all_characters.extend(data['results'])
        url = data['info']['next']
    
    # Filter: Human, Alive, from Earth
    filtered = []
    for char in all_characters:
        if (char['species'] == 'Human' and 
            char['status'] == 'Alive' and 
            'Earth' in char['origin']['name']):
            filtered.append({
                'name': char['name'],
                'location': char['location']['name'],
                'image': char['image']
            })
    
    return filtered


@app.route('/healthcheck', methods=['GET'])
@app.route('/health', methods=['GET'])
def healthcheck():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'rick-and-morty-api'
    }), 200


@app.route('/characters', methods=['GET'])
def get_characters():
    """Get all filtered characters."""
    try:
        characters = fetch_filtered_characters()
        return jsonify({
            'count': len(characters),
            'characters': characters
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/', methods=['GET'])
def index():
    """API documentation."""
    return jsonify({
        'service': 'Rick and Morty Character API',
        'endpoints': {
            '/characters': 'GET - Fetch all Human, Alive characters from Earth',
            '/healthcheck': 'GET - Health check endpoint',
            '/health': 'GET - Health check endpoint (alias)'
        }
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

