import unittest
from cohereflow.generator import generate_text

class TestGenerateText(unittest.TestCase):
    def test_generate_text(self):
        prompt = "Hello"
        model = "xlarge"
        max_tokens = 50
        min_length = 10
        max_length = 100
        required_keywords = ["world"]
        
        result = generate_text(prompt=prompt,
                               model=model,
                               max_tokens=max_tokens,
                               min_length=min_length,
                               max_length=max_length,
                               required_keywords=required_keywords)
        
        self.assertIsInstance(result, str)
        self.assertGreaterEqual(len(result), min_length)
        self.assertLessEqual(len(result), max_length)
        
if __name__ == '__main__':
    unittest.main()
