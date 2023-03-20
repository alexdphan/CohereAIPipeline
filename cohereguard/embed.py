from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import cohere
import os
import numpy as np

# load environment variables
from dotenv import load_dotenv
load_dotenv()

# Load your Cohere API key
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

app = FastAPI()
embed_router = APIRouter()

class EmbedInput(BaseModel):
    text: str

class EmbedConfig(BaseModel):
    model: str = "large"
    truncate: int = None

@embed_router.post("/embed")
async def get_embedding(input_data: EmbedInput, config: EmbedConfig = EmbedConfig()):
    model = config.model
    truncate = config.truncate
    response = co.embed(model=model, texts=[input_data.text], truncate=truncate)
    embeddings_array = np.array(response.embeddings)
    return {"embedding": embeddings_array[0].tolist()}

app.include_router(embed_router)

# ===============

# to customize the response, you can use the get_embedding function from cohereguard/embed.py to get the embedding for a single text input.
# The function takes a text input, a model name, and a truncate value as arguments.
# The model name can be either "small" or "large". The truncate value is the maximum number of tokens to use for the embedding.
# The function returns a dictionary with the embedding as a list of floats.

# ===============
# from my_package.cohere_embed import get_embedding, EmbedInput, EmbedConfig

# text = "I love this movie!"
# model = "large"
# truncate = 512

# # Using default values
# embedding = get_embedding(EmbedInput(text=text))
# print(embedding)

# # Using custom values
# embedding = get_embedding(EmbedInput(text=text), EmbedConfig(model=model, truncate=truncate))
# print(embedding)

