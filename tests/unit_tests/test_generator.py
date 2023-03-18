import os
from cohereflow.generator import generate_and_validate_text
from cohere.classify import Example
from cohereflow.models import GeneratedText
from cohereflow.validation import validate_text, is_valid_length, contains_required_keywords

def test_generate_and_validate_text():
    api_key = os.getenv("YOUR_API_KEY")
    assert api_key is not None, "API key is required"
    
    # Define classification and confidence score functions
    def compute_classification(text, examples):
        return "positive"
    
    def compute_confidence_score(text, examples):
        return 0.9
    
    # Call the function with test inputs
    generated_text = generate_and_validate_text(
    model="xlarge",
    prompt="Test prompt. I like chicken.",
    temperature=0.5,
    min_length=10,
    max_length=100,
    required_keywords=["chicken"],
    examples=[Example("cat", "animals"), Example("dog", "animals")],
    max_retries=3,
    compute_classification=compute_classification,
    compute_confidence_score=compute_confidence_score,
)

    is_valid = validate_text(generated_text.text, 10, 100, ["chicken"])
    contains_keywords = contains_required_keywords(generated_text.text, ["chicken"])
    valid_length = is_valid_length(generated_text.text, 10, 100)
    print(f"is_valid: {is_valid}")
    print(f"contains_keywords: {contains_keywords}")
    print(f"valid_length: {valid_length}")

    # Check that the function returns an instance of GeneratedText
    assert isinstance(generated_text, GeneratedText)

    # Check that the generated text matches the prompt
    assert generated_text.text.startswith("Test prompt.")

    # Check that the classification and confidence score are as expected
    assert generated_text.classification == "positive"
    assert generated_text.confidence_score == 0.9


# look at generator.py, try to see if its because of the api key, rate limiting, or something else
# E       ValueError: Failed to generate valid text after maximum retries
# >       raise ValueError("Failed to generate valid text after maximum retries")
# E       ValueError: Failed to generate valid text after maximum retries

# The test failed because the generate_and_validate_text() function was unable to generate valid text even after the maximum number of retries. You may need to adjust the parameters such as the prompt, required keywords, or model, or increase the maximum number of retries. Alternatively, you could modify the test case to generate text with a higher likelihood of success, or remove the test altogether if it's not critical for your code.

# It looks like the test is failing because it's unable to generate valid text that meets the criteria specified in the generate_and_validate_text() function. Specifically, it seems like it's failing to generate text that includes the required keyword "Test".

# You might want to try adjusting the prompt or required keywords to make it more likely that valid text can be generated. Alternatively, you could increase the number of max_retries in the generate_and_validate_text() function to give it more attempts to generate valid text.



