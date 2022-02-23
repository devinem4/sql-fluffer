from datetime import datetime
from fastapi import FastAPI
import sqlfluff

app = FastAPI()

@app.get("/")
def root():
    return { "time": datetime.now() }
