import unittest
from cohereguard.cohereguard_generate import generate_text
import guardrails as gd
from cohereguard.cohereguard_rail import rail_spec
import os

# import and set the RAIL spec from cohereguard_rail.py 
guard = gd.Guard.from_rail_string(rail_spec)

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

class TestCohereUtils(unittest.TestCase):
    def test_generate_text(self):
        api_key = COHERE_API_KEY
        model = "xlarge"
        prompt = "I like chicken nuggets"
        max_tokens = 500
        
        result = generate_text(model, prompt, max_tokens)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()


# import unittest
# from cohereguard.cohereguard_generate import generate_text
# import guardrails as gd
# from cohereguard.cohereguard_rail import rail_spec

# # # import and set the RAIL spec from cohereguard_rail.py
# guard = gd.Guard.from_rail_string(rail_spec)

# # # Compiles the RAIL output specification and adds it to the provided prompt.
# print(guard.base_prompt)

# class TestCohereUtils(unittest.TestCase):
#     def test_generate_text(self):
#         model = "xlarge"
#         prompt = f"""  
# This program generates a startup idea and name given the industry.

# Industry: Workplace  
# Startup Idea: A platform that generates slide deck contents automatically based on a given outline  
# Startup Name: Deckerize  
# --  
# Industry: Home Decor  
# Startup Idea: An app that calculates the best position of your indoor plants for your apartment  
# Startup Name: Planteasy
# --  
# Industry: Healthcare  
# Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week  
# Startup Name: Hearspan

# --  
# Industry: Education  
# Startup Idea: An online school that lets students mix and match their own curriculum based on their interests and goals  
# Startup Name: Prime Age

# --  
# Industry: Productivity  
# Startup Idea:"""
#         max_tokens = 500
        
#         result = generate_text(model, prompt, max_tokens)
#         print(result)
        
#         self.assertIsInstance(result, str)
#         self.assertGreater(len(result), 0)

# if __name__ == '__main__':
#     unittest.main()
