import os
import cohere
from dotenv import load_dotenv

load_dotenv()

# Load your Cohere API key
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

