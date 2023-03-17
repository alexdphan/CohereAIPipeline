from cohereflow.validation import contains_required_keywords, is_valid_length, contains_required_keywords, validate_text
import unittest

def test_is_valid_length():
    text = "Hello, world!"
    assert is_valid_length(text, 5, 20) == True
    assert is_valid_length(text, 1, 10) == False

def test_contains_requred_keywords():
    text = "The quick brown fox jumps over the lazy dog"
    required_keywords = ["fox", "dog"]
    assert contains_required_keywords(text, required_keywords) == True
    required_keywords = ["cat", "dog"]
    assert contains_required_keywords(text, required_keywords) == False

# Path: tests/unit_tests/test_validation.py

# with unittest package
class TestValidationFunctions(unittest.TestCase):
    def test_is_valid_length(self):
        self.assertTrue(is_valid_length("This is a valid text.", 5, 50))
        self.assertFalse(is_valid_length("This is an invalid text because it is too short.", 50, 100))
        self.assertFalse(is_valid_length("This is an invalid text because it is too long.", 5, 20))

    def test_contains_required_keywords(self):
        self.assertTrue(contains_required_keywords("This text contains example and validate keywords.", ["example", "validate"]))
        self.assertFalse(contains_required_keywords("This text contains only the example keyword.", ["example", "validate"]))

    def test_validate_text(self):
        self.assertTrue(validate_text("This example and validate keywords.", 5, 50, ["example", "validate"]))
        self.assertFalse(validate_text("This is an invalid text because it is too short with example and validate keywords, so we make it longer so it fits the limit.", 50, 100, ["example", "validate"]))
        self.assertFalse(validate_text("This is a valid text with only the example keyword.", 5, 50, ["example", "validate"]))

if __name__ == "__main__":
    unittest.main()