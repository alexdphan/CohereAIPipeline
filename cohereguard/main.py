from fastapi import FastAPI
import uvicorn

from cohereguard.classify import classify_router
from cohereguard.generate import generate_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(generate_router)
# embed
app.include_router(classify_router)
# tokenize
# detokenize
# detect-language
# summarize

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
