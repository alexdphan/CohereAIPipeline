import os
from typing import List
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from cohere.classify import Example
from cohere.client import Client
from spellchecker import SpellChecker

nltk.download('punkt')
nltk.download('stopwords')

co = Client(os.getenv("YOUR_API_KEY"))

# Define the examples (text and label pairs)
examples = [
    Example(text="The movie was absolutely fantastic!", label="Positive"),
    Example(text="I really enjoyed the film.", label="Positive"),
    Example(text="The film was terrible and boring.", label="Negative"),
    Example(text="I didn't like the movie at all.", label="Negative"),
]

# Download required resources
nltk.download('punkt') # for tokenization
nltk.download('stopwords') # for removing stopwords

# for spell correction (spellchecker library)
spell = SpellChecker(language='en')

def preprocess(text: str) -> str:
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]

    # for spell correction
    corrected_tokens = [spell.correction(w) for w in filtered_tokens]

    # Return the preprocessed text as a single string
    preprocessed_text = " ".join(corrected_tokens)
    return preprocessed_text

def classify(input_text: str) -> str:
    # Call the preprocess function
    preprocessed_text = preprocess(input_text)

    # Call the classify endpoint
    response = co.classify(model="large", inputs=[preprocessed_text], examples=examples)

    # Extract the classification result
    classification = response.classifications[0]

    # Get the highest confidence label and its score
    predicted_label, confidence_score = max(classification.labels.items(), key=lambda x: x[1])

    return predicted_label
