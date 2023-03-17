import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_special_characters(text: str) -> str:
    """
    Remove special characters from the input text.
    """
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', text)

def remove_stopwords(text: str) -> str:
    """
    Remove common stopwords from the input text.
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    return ' '.join([word for word in word_tokens if word.lower() not in stop_words])

