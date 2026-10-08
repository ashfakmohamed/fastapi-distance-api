import pytest
from fastapi.testclient import TestClient

from main import app, haversine_distance


client = TestClient(app)


def test_haversine_distance_between_new_york_and_los_angeles():
    distance = haversine_distance(40.7128, -74.0060, 34.0522, -118.2437)
    assert distance == pytest.approx(3935.75, rel=0.01)


def test_distance_endpoint_returns_kilometers():
    response = client.get(
        "/distance/",
        params={
            "lat1": 40.7128,
            "lon1": -74.0060,
            "lat2": 34.0522,
            "lon2": -118.2437,
        },
    )

    assert response.status_code == 200
    assert response.json()["unit"] == "km"
    assert response.json()["distance"] == pytest.approx(3935.75, rel=0.01)


def test_distance_endpoint_rejects_invalid_latitude():
    response = client.get(
        "/distance/",
        params={"lat1": 91, "lon1": 0, "lat2": 0, "lon2": 0},
    )

    assert response.status_code == 422
