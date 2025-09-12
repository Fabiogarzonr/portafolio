# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import os


from logica_pdf import procesar_pdfs

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")



@app.post("/procesar/")
async def procesar_archivos(files: List[UploadFile] = File(...)):
    rutas = []
    for file in files:
        ruta = os.path.join(UPLOAD_DIR, file.filename)
        with open(ruta, "wb") as f:
            f.write(await file.read())
        rutas.append(ruta)

    resultado = procesar_pdfs(rutas)
    return JSONResponse(content=resultado)



@app.get("/", response_class=HTMLResponse)
def home():
    with open("formulario.html", encoding="utf-8") as f:
        return f.read()



@app.get("/etiqueta", response_class=HTMLResponse)
def etiqueta():
    with open("etiqueta.html", encoding="utf-8") as f:
        return f.read()
