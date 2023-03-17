import unittest
from cohereflow.models import GeneratedText

class TestGeneratedText(unittest.TestCase):
    def test_generated_text_creation(self):
        text = "This is an example text."
        classification = "example_classification"
        confidence_score = 0.9

        generated_text = GeneratedText(text=text, classification=classification, confidence_score=confidence_score)

        self.assertEqual(generated_text.text, text)
        self.assertEqual(generated_text.classification, classification)
        self.assertEqual(generated_text.confidence_score, confidence_score)

if __name__ == "__main__":
    unittest.main()
