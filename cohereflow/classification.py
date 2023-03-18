import os
from cohere.classify import Example
import cohere
from typing import List

# import environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Load your Cohere API key from environment variable
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Raise an error if the API key is not found
if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found in environment variables.")


def get_classification_results(text: str, examples: List[Example], model: str = "large") -> dict:
    response = co.classify(model=model, inputs=[text], examples=examples)
    classification = response.classifications[0]
    predicted_label, confidence_score = max(classification.labels.items(), key=lambda x: x[1])
    return {
        "predicted_label": predicted_label,
        "confidence_score": confidence_score.confidence
    }

def compute_classification(text: str, examples: List[Example]) -> str:
    results = get_classification_results(text, examples)
    return results["predicted_label"]

def compute_confidence_score(text: str, examples: List[Example]) -> float:
    results = get_classification_results(text, examples)
    return results["confidence_score"]

# contains functions get_classification_results, compute_classification, and compute_confidence_score
    # get_classification_results: takes in text and examples and returns a dictionary with predicted_label and confidence_score
    # compute_classification: takes in text and examples and returns a string of the predicted_label
    # compute_confidence_score: takes in text and examples and returns a float of the confidence_score