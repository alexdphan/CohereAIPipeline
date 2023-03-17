# from fastapi import FastAPI
# import uvicorn

# from cohereflow.preprocess import remove_special_characters, remove_stopwords

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World!"}

# app.include_router(remove_special_characters)
# app.include_router(remove_stopwords)

# # Run the app
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)

from cohereflow.preprocess import remove_special_characters, remove_stopwords

# Now you can call the functions in your code
text = "Hello, world! This is some example text."
text_without_special_chars = remove_special_characters(text)
text_without_stopwords = remove_stopwords(text_without_special_chars)
print(text_without_stopwords)
