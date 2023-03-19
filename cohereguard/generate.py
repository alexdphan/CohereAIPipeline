from dotenv import load_dotenv
from fastapi import APIRouter, Query
import cohere
import os

# Load the environment variables from the .env file
load_dotenv()

# Load your Cohere API key
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

generate_router = APIRouter()

@generate_router.get("/generate")
async def generate(
    model: str,
    prompt: str,
    max_tokens: int = Query(1024),
    temperature: float = Query(1.0),
):
    response = co.generate(model=model, prompt=prompt, max_tokens=max_tokens,
                           temperature=temperature)

    return {"generated_text": response.generations[0].text}