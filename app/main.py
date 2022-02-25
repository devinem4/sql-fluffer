from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import sqlfluff

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/js", StaticFiles(directory="app/js"), name="js")
sqlfluff_config = ".sqlfluff"

class Sql(BaseModel):
    sql: str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("fluff.html", {"request": request})


@app.post("/fluff/")
async def fluff(sql: Sql):
    try:
        fixed = sqlfluff.fix(
            sql.sql,
            dialect="ansi",
            config_path=sqlfluff_config,
        )
        lint = sqlfluff.lint(
            fixed,
            dialect="ansi",
            config_path=sqlfluff_config,
        )
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
