from pydantic import BaseModel, Field

class GeneratedText(BaseModel):
    text: str = Field(..., description="Generated text")
    classification: str = Field(..., description="Classification of the generated text")
    confidence_score: float = Field(..., description="Confidence score of the classification")

    # GeneratedText is a custom data class that inherits from BaseModel.
    
        # BaseModel is a base class provided by the Pydantic library in Python. Pydantic is a data validation and parsing library that simplifies the process of validating, parsing, and serializing data in Python.

    # It has three fields: text, classification, and confidence_score, each with a specified data type and an optional description.

