from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from cohereguard.generate import (
    generate_router,
)  # Replace with the actual path to your generate_router

app = FastAPI()
app.include_router(generate_router)


@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)


def test_generate(test_client):
    model = "xlarge"
    prompt = "To be or not to be, that is the question"
    max_tokens = 50
    temperature = 0.8

    response = test_client.get(
        "/generate",
        params={
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        },
    )

    assert response.status_code == 200

    json_response = response.json()

    # You can add more assertions here based on the expected response format.

    assert "generated_text" in json_response
    assert isinstance(json_response["generated_text"], str)
    # For example, you can assert that the generated text is a string.
    assert json_response["generated_text"] != ""
    # You can also assert that the generated text is not the same as the prompt.
    assert json_response["generated_text"] != prompt
