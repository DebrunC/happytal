import json
import pytest


def test_getRecommendationByClient():
    data = {
        "user_id": 10,
        "numReco" : 
    }
    response = client.post("/model/recommendation/{idUser}",json.dumps(data))
    assert response.status_code == 200