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

def generate_text(model, prompt, max_tokens):
# Wrap the generate call with guard
    raw_llm_output, validated_output = guard(co.generate, model=model, prompt=prompt, max_tokens=max_tokens)

# Get the text from the response
    text = validated_output.generations[0].text

    return text

# 1. format the output in guardrails spec <output>
#     <pythoncode
#         name="python_code"
#         format="cohere-python-generate"
#         on-fail-cohere-python-generate="reask"
#     />
    # might need to remove this since it's just the prompt... 
    # API Key: {{api_key}}
    # Model: {{model}}
    # Prompt: {{prompt}}
    # Max Tokens: {{max_tokens}}  
# </output>
# 2. Wrap the function with guardrails




# 2. validate the output with guardrails
# 3. if validation fails, reask the user for input
# 4. if validation passes, return the output
# 5. if the user wants to quit, return None





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
