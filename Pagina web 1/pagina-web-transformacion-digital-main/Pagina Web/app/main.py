from pathlib import Path
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Portafolio de Transformación Digital")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def cargar_perfil():
    archivo = BASE_DIR / "data" / "perfil.json"
    return json.loads(archivo.read_text(encoding="utf-8"))


@app.get("/", response_class=HTMLResponse)
async def perfil(request: Request):
    perfil = cargar_perfil()
    return templates.TemplateResponse("perfil.html", {"request": request, "perfil": perfil})
