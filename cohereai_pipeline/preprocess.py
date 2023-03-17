import os
from fastapi import FastAPI, Query, APIRouter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import cohere
from dotenv import load_dotenv
from cohere.classify import Example
from spellchecker import SpellChecker


# Load environment variables
load_dotenv()

# Load Cohere API Key
COHERE_API_KEY = os.getenv("YOUR_API_KEY")

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

examples = [
    Example(text="Example 1", label="Label 1"),
    Example(text="Example 2", label="Label 1"),
    Example(text="Example 1", label="Label 2"),
    Example(text="Example 2", label="Label 2"),
]

preprocess_router = APIRouter()

@preprocess_router.get("/preprocess")
async def preprocess(text: str = Query(..., description="The text to preprocess")):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    # sets stop_words to a list of stopwords from the english language like "the", "a", "an", etc.
    filtered_tokens = [w for w in tokens if not w in stop_words]
    # sets filtered_tokens to a list of words that are not in stop_words

   # for spell correction (spellchecker library)
    spell = SpellChecker(language='en')
    corrected_tokens = [spell.correction(w) for w in filtered_tokens]

    # Return the preprocessed text as a single string
    preprocessed_text = " ".join(corrected_tokens)
    return preprocessed_text

    # Return the preprocessed text as a single string
    preprocessed_text = " ".join(filtered_tokens)
    return {"preprocessed_text": preprocessed_text}


