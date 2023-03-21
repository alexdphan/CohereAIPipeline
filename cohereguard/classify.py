from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel
from cohere.responses.classify import Example
from cohereguard.config import co

app = FastAPI()
classify_router = APIRouter()

class ClassifyInput(BaseModel):
    """
    A Pydantic model representing input data for classification.

    Attributes:
        text (str): The input text to be classified.
    """

    text: str


class ClassifyConfig(BaseModel):
    """
    A Pydantic model representing configuration options for classification.

    Attributes:
        model (str): The name of the classification model to use (either "small" or "large").
    """

    model: str = "large"


@classify_router.post("/classify")
async def classify(input_data: ClassifyInput, config: ClassifyConfig = ClassifyConfig()):
    """
    Classifies the input text using the Cohere API.

    Args:
        input_data (ClassifyInput): A Pydantic model representing the input text to classify.
        config (ClassifyConfig): A Pydantic model representing the configuration options for classification.

    Returns:
        A dictionary with the input text, predicted label, and confidence score.
    """
    # Define the examples (text and label pairs)
    examples = [
        Example(text="The movie was absolutely fantastic!", label="Positive"),
        Example(text="I really enjoyed the film.", label="Positive"),
        Example(text="The film was terrible and boring.", label="Negative"),
        Example(text="I didn't like the movie at all.", label="Negative"),
        Example(text="The movie was okay.", label="Neutral"),
        Example(text="The movie was just okay.", label="Neutral"),
    ]

    # Call the classify endpoint
    response = co.classify(model=config.model, inputs=[input_data.text], examples=examples)

    # Extract the classification result
    classification = response.classifications[0]

    # Get the highest confidence label and its score
    predicted_label, confidence_score = max(
        classification.labels.items(), key=lambda x: x[1]
    )

    # Return the input text, predicted label, and confidence score as a JSON response
    return {
        "input_text": input_data.text,
        "predicted_label": predicted_label,
        "confidence_score": confidence_score,
    }

## Example Use Case of Classify Endpoint

# from cohereguard import classify

# Initialize the Cohere API with your API key
# co = cohere.Client("YOUR_API_KEY")

# Define the input text and classification model
# text = "The movie was amazing!"
# model = "large"

# Classify the input text
# classification_result = classify(text, model, co)

# Print the result
# print(classification_result)


