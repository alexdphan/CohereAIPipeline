from cohereflow.validation import is_valid_length, contains_requred_keywords

def test_is_valid_length():
    text = "Hello, world!"
    assert is_valid_length(text, 5, 20) == True
    assert is_valid_length(text, 1, 10) == False

def test_contains_requred_keywords():
    text = "The quick brown fox jumps over the lazy dog"
    required_keywords = ["fox", "dog"]
    assert contains_requred_keywords(text, required_keywords) == True
    required_keywords = ["cat", "dog"]
    assert contains_requred_keywords(text, required_keywords) == False
