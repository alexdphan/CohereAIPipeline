import cohere
import os
import guardrails as gd
from cohereguard.cohereguard_rail import rail_spec

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Load your Cohere API key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Create a Cohere client
co = cohere.Client(COHERE_API_KEY)

# import and set the RAIL spec from cohereguard_rail.py
guard = gd.Guard.from_rail_string(rail_spec)

# Compiles the RAIL output specification and adds it to the provided prompt.
print(guard.base_prompt)

def generate_text(model, prompt, max_tokens):
    # Call Cohere's generate endpoint with desired settings
    response = co.generate(model=model, prompt=prompt, max_tokens=max_tokens)
    text = response.generations[0].text
    
    return text




# generate_text() is a wrapper function prompts the user for input if arguments are not provided
# It also that calls the Cohere API and validates the generated text by calling validate_text()
# validate_text() is a wrapper function that calls the Cohere API and validates the generated text by calling validate_text()



# import os
# import guardrails as gd
# from cohereguard_rail import rail_str
# from rich import print
# import cohere

# from dotenv import load_dotenv

# load_dotenv()

# # creating a Guard object with the RAIL Spec

# guard = gd.Guard.from_rail_string(rail_str)

# # Print/Compile the output schema and add it to the prompt
# print(guard.base_prompt)

# # Load your Cohere API key
# COHERE_API_KEY = os.getenv("YOUR_API_KEY")
# co = cohere.Client(COHERE_API_KEY)

# # Set the model, prompt, and max tokens
# model = "baseline-shrimp"
# prompt = "Once upon a time in a small village, "
# max_tokens = 50

# # Call the generate endpoint
# response = co.generate(model, prompt, max_tokens=max_tokens)

# # Extract and print the generated text
# generated_text = response["generated_text"]
# print(generated_text)
