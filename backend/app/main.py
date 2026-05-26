from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DeepFake Detection API Running"}