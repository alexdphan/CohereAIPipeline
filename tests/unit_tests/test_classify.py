from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from cohereguard.classify import classify_router  # Replace with the actual path to your classify_router

app = FastAPI()
app.include_router(classify_router)

client = TestClient(app)

def test_classify():
    response = client.post("/classify", params={"input_text": "The movie was great!"})
    assert response.status_code == 200
    assert response.json() == {
        "input_text": "The movie was great!",
        "predicted_label": "Positive",
        "confidence_score": [pytest.approx(0.99, abs=0.1)],
        # classifying a single example returns a list of confidence scores
    }

def test_classify_positive():
    response = client.post("/classify", params={"input_text": "I love this movie!"})
    assert response.status_code == 200
    assert response.json() == {
        "input_text": "I love this movie!",
        "predicted_label": "Positive",
        "confidence_score": [pytest.approx(0.9737713, abs=0.1)],
    }

def test_classify_negative():
    response = client.post("/classify", params={"input_text": "I hate this movie!"})
    assert response.status_code == 200
    assert response.json() == {
        "input_text": "I hate this movie!",
        "predicted_label": "Negative",
        "confidence_score": [pytest.approx(0.8905472, abs=0.1)],
    }

def test_classify_neutral():
    response = client.post("/classify", params={"input_text": "This movie is okay."})
    assert response.status_code == 200
    assert response.json() == {
        "input_text": "This movie is okay.",
        "predicted_label": "Neutral",
        "confidence_score": [pytest.approx(0.99780536, abs=0.1)],
    }


# # In the pytest.approx() function, the abs parameter specifies the maximum absolute difference between the expected value and the actual value.


# to be more optimized/use pytest fixtures
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# import pytest

# from cohereguard.classify import classify_router

# app = FastAPI()
# app.include_router(classify_router)

# @pytest.fixture(scope="module")
# def test_client():
#     return TestClient(app)

# @pytest.mark.parametrize(
#     "input_text, predicted_label, expected_confidence",
#     [
#         ("The movie was great!", "Positive", 0.99),
#         ("I love this movie!", "Positive", 0.9737713),
#         ("I hate this movie!", "Negative", 0.8905472),
#         ("This movie is okay.", "Neutral", 0.99780536),
#     ],
# )
# def test_classify(test_client, input_text, predicted_label, expected_confidence):
#     response = test_client.post("/classify", params={"input_text": input_text})
#     assert response.status_code == 200
#     assert response.json() == {
#         "input_text": input_text,
#         "predicted_label": predicted_label,
#         "confidence_score": [pytest.approx(expected_confidence, abs=0.1)],
#     }
