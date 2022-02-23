from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlfluff

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def root():
    return { "time": datetime.now() }

@app.get("/fluff", response_class=HTMLResponse)
async def fluff(request: Request):
    return templates.TemplateResponse("fluff.html", {"request": request})

