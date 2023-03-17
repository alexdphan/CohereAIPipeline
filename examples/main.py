from fastapi import FastAPI
import uvicorn

from cohereflow.preprocess import remove_special_characters, remove_stopwords

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(remove_special_characters)
app.include_router(remove_stopwords)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)