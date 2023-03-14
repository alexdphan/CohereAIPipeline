from fastapi import FastAPI

coolapp = FastAPI()


@coolapp.get("/")
async def root():
    return {"message": "yomama"}

# could also be written as
# coolapp = FastAPI()
# coolapp.get("/")(root)
    # def root():
    #     return {"message": "yomama"}

    # uvicorn main:coolapp --reload                  