import pytest
from flask import json
from unittest.mock import patch
from app import app
import requests


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_weather_endpoint_success(client):
    mock_weather_data = {
        "name": "Beijing",
        "main": {
            "temp": 20,
            "humidity": 50
        },
        "weather": [
            {"description": "clear sky"}
        ],
        "wind": {
            "speed": 3.5
        }
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_weather_data
        mock_get.return_value.raise_for_status.return_value = None

        response = client.get('/api/weather?city=Beijing')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['city'] == 'Beijing'
        assert data['temperature'] == 20
        assert data['description'] == 'clear sky'
        assert data['humidity'] == 50
        assert data['wind_speed'] == 3.5


def test_weather_endpoint_missing_city(client):
    response = client.get('/api/weather')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'City parameter is required'


def test_weather_endpoint_api_error(client):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("API Error")

        response = client.get('/api/weather?city=Beijing')

        assert response.status_code == 500
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'Failed to fetch weather data'


def test_weather_endpoint_invalid_city(client):
    mock_error_response = {
        "cod": "404",
        "message": "city not found"
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_error_response
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("404 Client Error: Not Found")

        response = client.get('/api/weather?city=InvalidCity')

        assert response.status_code == 500
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'Failed to fetch weather data'