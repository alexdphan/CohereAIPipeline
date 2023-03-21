# import os
from enum import Enum
from fastapi import FastAPI, APIRouter
import numpy as np

# load environment variables
# from dotenv import load_dotenv
from pydantic import BaseModel
from cohereguard.config import co

embed_router = APIRouter()

class EmbedInput(BaseModel):
    """
    A Pydantic model representing input data for embedding.

    Attributes:
        text (str): The input text to be embedded.
    """

    text: str

class TruncateOptions(str, Enum):
    NONE = "NONE"
    START = "START"
    END = "END"


class EmbedConfig(BaseModel):
    """
    A Pydantic model representing configuration options for embedding.

    Attributes:
        model (str): The name of the embedding model to use (either "small" or "large").
        truncate (int): The maximum number of tokens to use for the embedding.
    """

    model: str = "large"
    truncate: TruncateOptions = TruncateOptions.END

@embed_router.post("/embed")
async def get_embedding(input_data: EmbedInput, config: EmbedConfig = EmbedConfig()):
    """
    Generates an embedding for the input text using the Cohere API.

    Args:
        input_data (EmbedInput): A Pydantic model representing the input text to embed.
        config (EmbedConfig): A Pydantic model representing the configuration options for embedding.

    Returns:
        A dictionary with the embedding as a list of floats.
    """
    model = config.model
    truncate = config.truncate
    
    response = co.embed(model=model, texts=[input_data.text], truncate=truncate)
    
    embeddings_array = np.array(response.embeddings)
    return {"embedding": embeddings_array[0].tolist()}

## Example Use Case of Embedding Endpoint

# Import the necessary classes and functions from your package
# from cohereguard.embed import EmbedInput, EmbedConfig, get_embedding

# Initialize Cohere API client with your API key
# co = cohere.Client("YOUR_API_KEY")

# Define the input text to be embedded
# text = "I love this movie!"

# Call the get_embedding function with default configuration
# embedding = get_embedding(EmbedInput(text=text))

# Print the embedding
# print(embedding)

# Call the get_embedding function with custom configuration
# model = "small"
# truncate = 128
# embedding = get_embedding(EmbedInput(text=text), EmbedConfig(model=model, truncate=truncate))

# Print the embedding
# print(embedding)




