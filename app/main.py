from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import sqlfluff

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

class Sql(BaseModel):
    sql: str

@app.get("/")
def root():
    return { "time": datetime.now() }


@app.post("/lint/")
async def lint(sql: Sql):
    try:
        fixed = sqlfluff.fix(sql.sql, dialect="ansi", fix_even_unparsable=True)
        lint = sqlfluff.lint(fixed, dialect="ansi")
    except:
        return {
            "original": sql.sql,
            "error": True
        }
    return {
      "original": sql.sql,
      "fixed": fixed,
      "lint": lint
    }


@app.get("/fluff/", response_class=HTMLResponse)
async def fluff(request: Request):
    return templates.TemplateResponse("fluff.html", {"request": request})

