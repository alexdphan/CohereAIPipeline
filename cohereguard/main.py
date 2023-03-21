from fastapi import FastAPI
import uvicorn

from cohereguard.classify import classify_router
from cohereguard.generate import generate_router
from cohereguard.embed import embed_router
from cohereguard.tokenize import tokenize_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(generate_router)
app.include_router(embed_router)
app.include_router(classify_router)
app.include_router(tokenize_router)
# detokenize
# detect-language
# summarize

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
