import cohere
from cohereflow.validation import validate_text
import os

# import environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Load your Cohere API key from environment variable
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_text(prompt=None, model=None, max_tokens=None, min_length=None, max_length=None, required_keywords=None):
    # Prompt user for input if arguments are not provided
    if prompt is None:
        prompt = input("Enter a prompt: ")
    
    if model is None:
        model = input("Enter a model (default: xlarge): ") or "xlarge"
    
    if max_tokens is None:
        max_tokens = int(input("Enter max tokens (default: 50): ") or 50)
    
    if min_length is None:
        min_length = int(input("Enter minimum length (default: 10): ") or 10)
    
    if max_length is None:
        max_length = int(input("Enter maximum length (default: 100): ") or 100)
    
    if required_keywords is None:
        required_keywords = input("Enter required keywords separated by commas (default: none): ").split(",")
    
    # Call Cohere's generate endpoint with desired settings
    response = co.generate(model=model, prompt=prompt, max_tokens=max_tokens)
    text = response.generations[0].text
    
    # Check if generated text passes validation
    if not validate_text(text, min_length, max_length, required_keywords):
        # Implement corrective actions such as re-prompting the model with a modified prompt or adjusting temperature or max tokens
        text = "Fallback response"
    
    return text

# generate_text() is a wrapper function prompts the user for input if arguments are not provided
# It also that calls the Cohere API and validates the generated text by calling validate_text()
# validate_text() is a wrapper function that calls the Cohere API and validates the generated text by calling validate_text()