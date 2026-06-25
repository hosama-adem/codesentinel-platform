import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CodeSentinel API Running", "db": os.getenv("DATABASE_URL")}
