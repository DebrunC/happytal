import pytest
from fastapi.testclient import TestClient
from main import app  


client = TestClient(app)

def test_getRecommendationByClient():
	response = client.get("/model/recommendation/10")
	assert response.status_code == 200


def test_hello_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to the recommender system app"}

