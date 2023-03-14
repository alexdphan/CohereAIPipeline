from fastapi import FastAPI, Query
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = FastAPI()

@app.get("/preprocess")
async def preprocess(text: str = Query(..., description="The text to preprocess")):
    # Download required resources
    nltk.download('punkt')
    nltk.download('stopwords')
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    
    # Return the preprocessed text
    return {"result": filtered_tokens}