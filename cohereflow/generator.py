import os
from typing import List, Callable
import cohere
from cohere.classify import Example
from cohereflow.models import GeneratedText
from cohereflow.validation import validate_text
from cohereflow.classification import compute_classification, compute_confidence_score
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YOUR_API_KEY")

if api_key is None:
    raise ValueError("API key is required")

def generate_and_validate_text(
    model: str,
    prompt: str,
    temperature: float,
    min_length: int,
    max_length: int,
    required_keywords: List[str],
    examples: List[Example],
    compute_classification: Callable[[str, List[Example]], str],
    compute_confidence_score: Callable[[str, List[Example]], float],
    max_retries: int = 3,
) -> GeneratedText:
    co = cohere.Client(api_key)

    print("Generating text...")

    for _ in range(max_retries):
        response = co.generate(model=model, prompt=prompt, temperature=temperature, max_tokens=max_length)
        generated_text = response.generations[0].text

        if validate_text(generated_text, min_length, max_length, required_keywords):
            classification = compute_classification(generated_text, examples)
            confidence_score = compute_confidence_score(generated_text, examples)
            return GeneratedText(text=generated_text, classification=classification, confidence_score=confidence_score)

        # Modify the prompt, temperature, or max_tokens if necessary
        # prompt = ...

    raise ValueError("Failed to generate valid text after maximum retries")

def main():
    # Take user inputs for all necessary parameters
    model = input("Please enter the model: ")
    prompt = input("Please enter the prompt: ")
    temperature = float(input("Please enter the temperature: "))
    min_length = int(input("Please enter the minimum length: "))
    max_length = int(input("Please enter the maximum length: "))
    required_keywords = input("Please enter the required keywords (comma-separated): ").split(",")
    max_retries = int(input("Please enter the maximum retries: "))

    # Define the examples for classification
    examples = [
        Example("cat", "animals"),
        Example("dog", "animals"),
    ]

    # Call generate_and_validate_text() function with the user inputs
    generated_text = generate_and_validate_text(
        model=model,
        prompt=prompt,
        temperature=temperature,
        min_length=min_length,
        max_length=max_length,
        required_keywords=required_keywords,
        examples=examples,
        compute_classification=compute_classification,
        compute_confidence_score=compute_confidence_score,
        max_retries=max_retries,
    )

    # Print the generated text, classification, and confidence score
    print(f"Generated Text: {generated_text.text}")
    print(f"Classification: {generated_text.classification}")
    print(f"Confidence Score: {generated_text.confidence_score}")

if __name__ == "__main__":
    main()


# import os
# import requests
# from typing import List, Callable
# from cohereflow.models import GeneratedText
# from cohereflow.validation import validate_text
# from cohereflow.classification import compute_classification, compute_confidence_score
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("YOUR_API_KEY")

# if api_key is None:
#     raise ValueError("API key is required")

# def generate_and_validate_text(
#     model: str,
#     prompt: str,
#     temperature: float,
#     min_length: int,
#     max_length: int,
#     required_keywords: List[str],
#     compute_classification: Callable[[str], str],
#     compute_confidence_score: Callable[[str], float],
#     max_retries: int = 3,
# ) -> GeneratedText:

#     base_url = "https://api.cohere.ai"

#     for _ in range(max_retries):
#         response = requests.post(
#             f"{base_url}/v1/{model}/generate",
#             json={
#                 "prompt": prompt,
#                 "temperature": temperature,
#                 "max_tokens": max_length,
#             },
#             headers={"Authorization": f"Bearer {api_key}"},
#         )
#         response.raise_for_status()
#         data = response.json()
#         generated_text = data["generated"]

#         if validate_text(generated_text, min_length, max_length, required_keywords):
#             classification = compute_classification(generated_text)
#             confidence_score = compute_confidence_score(generated_text)
#             return GeneratedText(text=generated_text, classification=classification, confidence_score=confidence_score)

#         # Modify the prompt, temperature, or max_tokens if necessary
#         # prompt = ...

#     raise ValueError("Failed to generate valid text after maximum retries")

# def main():
#     # Take user inputs for all necessary parameters
#     model = "command-xlarge-nightly"
#     prompt = input("Please enter the prompt: ")
#     temperature = float(input("Please enter the temperature: "))
#     min_length = int(input("Please enter the minimum length: "))
#     max_length = int(input("Please enter the maximum length: "))
#     required_keywords = input("Please enter the required keywords (comma-separated): ").split(",")
#     max_retries = int(input("Please enter the maximum retries: "))

#     # Call generate_and_validate_text() function with the user inputs
#     generated_text = generate_and_validate_text(
#         model=model,
#         prompt=prompt,
#         temperature=temperature,
#         min_length=min_length,
#         max_length=max_length,
#         required_keywords=required_keywords,
#         compute_classification=compute_classification,
#         compute_confidence_score=compute_confidence_score,
#         max_retries=max_retries,
#     )

#     # Print the generated text, classification, and confidence score
#     print(f"Generated Text: {generated_text.text}")
#     print(f"Classification: {generated_text.classification}")
#     print(f"Confidence Score: {generated_text.confidence_score}")

# if __name__ == "__main__":
#     main()
