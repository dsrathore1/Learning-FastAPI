from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="Static"), name="Static")
templates = Jinja2Templates(directory="Templates")


@app.get("/")
async def get_data():
    return {
        "message": "Hello, I am learning FastAPI",
        "main-page": "http://127.0.0.1:8000/template",
    }


@app.get("/template", response_class=HTMLResponse)
async def get_template(request: Request):
    return templates.TemplateResponse(request=request, name="template.html")
