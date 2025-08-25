from fastapi import FastAPI

app = FastAPI(title="Film/Dizi Öneri API", version="0.1.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Quantique API"}