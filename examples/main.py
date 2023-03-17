from fastapi import FastAPI
import uvicorn
from classify import classify_router
from preprocess import preprocess_router
from preprocess_and_classify import preprocess_and_classify_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(classify_router)
app.include_router(preprocess_router)
app.include_router(preprocess_and_classify_router)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)