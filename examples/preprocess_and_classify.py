import os
from fastapi import APIRouter, FastAPI, Query
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import cohere
from dotenv import load_dotenv
from cohere.classify import Example
from spellchecker import SpellChecker
# from cohereflow.validation import GeneratedText, is_valid_length, contains_required_keywords

# Load environment variables
load_dotenv()

# Get the API key from the environment
COHERE_API_KEY = os.getenv("YOUR_API_KEY")
co = cohere.Client(COHERE_API_KEY)

nltk.download('punkt')
nltk.download('stopwords')

# Define the API router
preprocess_and_classify_router = APIRouter()

# Download required resources
nltk.download('punkt') # for tokenization
nltk.download('stopwords') # for removing stopwords

# Define the examples (text and label pairs)
examples = [
    Example(text="The movie was absolutely fantastic!", label="Positive"),
    Example(text="I really enjoyed the film.", label="Positive"),
    Example(text="The film was terrible and boring.", label="Negative"),
    Example(text="I didn't like the movie at all.", label="Negative"),
]

async def preprocess(text: str):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]

    # for spell correction (spellchecker library)
    spell = SpellChecker(language='en')
    corrected_tokens = [spell.correction(w) for w in filtered_tokens]

    # Return the preprocessed text as a single string
    preprocessed_text = " ".join(corrected_tokens)
    return preprocessed_text

@preprocess_and_classify_router.post("/preprocess_and_classify")
async def preprocess_and_classify(input_text: str = Query(..., description="The text to preprocess and classify")):
    # Call the preprocess function
    preprocessed_text = await preprocess(input_text)

    # Call the classify endpoint
    response = co.classify(model="large", inputs=[preprocessed_text], examples=examples)

    # Extract the classification result
    classification = response.classifications[0]

    # Get the highest confidence label and its score
    predicted_label, confidence_score = max(classification.labels.items(), key=lambda x: x[1])

    # Return the input text, preprocessed text, predicted label, and confidence score as a JSON response
    return {
        "input_text": input_text,
        "preprocessed_text": preprocessed_text,
        "predicted_label": predicted_label,
        "confidence_score": confidence_score,
    }
