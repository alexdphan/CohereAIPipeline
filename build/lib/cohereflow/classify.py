import os
import cohere
from cohere.classify import Example
from typing import List

# import environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# error because of missing API key, see below

# Load your Cohere API key from environment variable
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Define the examples (text and label pairs)
examples = [
    Example(text="The movie was absolutely fantastic!", label="Positive"),
    Example(text="I really enjoyed the film.", label="Positive"),
    Example(text="The film was terrible and boring.", label="Negative"),
    Example(text="I didn't like the movie at all.", label="Negative"),
]

def classify_text(text: str) -> dict:
    # Call the classify endpoint
    response = co.classify(model="large", inputs=[text], examples=examples)

    # Extract the classification result
    classification = response.classifications[0]

    # Get the highest confidence label and its score
    predicted_label, confidence_score = max(classification.labels.items(), key=lambda x: x[1])

    # Return the input text, predicted label, and confidence score as a dictionary
    return {
        "input_text": text,
        "predicted_label": predicted_label,
        "confidence_score": confidence_score,
    }
