from cohere.classify import Example
from cohereflow.validation import contains_required_keywords, is_valid_length

from cohereflow.preprocess import remove_special_characters, remove_stopwords

def test_preprocessing_functions():
    # Define the examples to use for classification
    examples = [
        Example(text="This is a positive example", label="positive"),
        Example(text="This is a negative example", label="negative"),
        Example(text="This is a neutral example", label="neutral"),
    ]
    # Define the text to preprocess
    text = "This is a    sample text with punctuation!!!"

    # Preprocess the text
    preprocessed_text = remove_special_characters(text)
    preprocessed_text = remove_stopwords(preprocessed_text)

    # Check if the preprocessed text is valid
    assert is_valid_length(preprocessed_text, 5, 50) == True
    assert contains_required_keywords(preprocessed_text, ["sample", "text"]) == True
