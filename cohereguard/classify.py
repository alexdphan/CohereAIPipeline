# Just a simple example of how to use the Cohere api to classify text, not necessary for the project
import os
from fastapi import FastAPI, Query, APIRouter
import cohere
from cohere.classify import Example
from typing import List
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Load your Cohere API key
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Define the examples (text and label pairs)
examples = [
    Example(text="The movie was absolutely fantastic!", label="Positive"),
    Example(text="I really enjoyed the film.", label="Positive"),
    Example(text="The film was terrible and boring.", label="Negative"),
    Example(text="I didn't like the movie at all.", label="Negative"),
    Example(text="The movie was okay.", label="Neutral"),
    Example(text="The movie was just okay.", label="Neutral"),
]

classify_router = APIRouter()

@classify_router.post("/classify")
async def classify(input_text: str = Query(..., description="The text to classify")):
    # Call the classify endpoint
    response = co.classify(model="large", inputs=[input_text], examples=examples)

    # Extract the classification result
    classification = response.classifications[0]

    # Get the highest confidence label and its score
    predicted_label, confidence_score = max(classification.labels.items(), key=lambda x: x[1])

    # Return the input text, predicted label, and confidence score as a JSON response
    return {
        "input_text": input_text,
        "predicted_label": predicted_label,
        "confidence_score": confidence_score,
    }
