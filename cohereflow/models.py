from pydantic import BaseModel, Field

class GeneratedText(BaseModel):
    text: str = Field(..., description="Generated text")
    classification: str = Field(..., description="Classification of the generated text")
    confidence_score: float = Field(..., description="Confidence score of the classification")