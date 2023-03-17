from pydantic import BaseModel, Field

class GeneratedText(BaseModel):
    text: str = Field(..., description="Generated text")
    classification: str = Field(..., description="Classification of the generated text")
    confidence_score: float = Field(..., description="Confidence score of the classification")


def is_valid_length(text: str, min_length: int, max_length: int) -> bool:
      """Check if the text is between the minimum and maximum length"""
      return min_length <= len(text) <= max_length

def contains_requred_keywords(text: str, required_keywords: list[str]) -> bool:
      """Check if the text contains all the required keywords"""
      return all(keyword in text for keyword in required_keywords)

# code checks if the text is between the minimum and maximum length, and if the text contains all the required keywords
def validate_text(text: str, min_length: int, max_length: int, required_keywords: list[str]) -> bool:
      """Check if the text is between the minimum and maximum length, and if the text contains all the required keywords"""
      return is_valid_length(text, min_length, max_length) and contains_requred_keywords(text, required_keywords)
