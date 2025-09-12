# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import os

from logica_pdf import procesar_pdfs

app = FastAPI()

# =============================
#        CONFIGURACIÓN
# =============================

# 🔹 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Directorio para uploads
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🔹 Servir imágenes estáticas
app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")

# 🔹 Carpeta de templates (HTML)
TEMPLATES_DIR = "templates"


# =============================
#          ENDPOINTS
# =============================

# 📌 Procesar PDFs
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


# =============================
#          RUTAS HTML
# =============================

# 📌 Página principal -> index.html
@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse(os.path.join(TEMPLATES_DIR, "index.html"))

# 📌 Página de formulario -> formulario.html
@app.get("/formulario", response_class=HTMLResponse)
def formulario():
    return FileResponse(os.path.join(TEMPLATES_DIR, "formulario.html"))

# 📌 Página de hoja de vida -> cv.html
@app.get("/cv", response_class=HTMLResponse)
def cv():
    return FileResponse(os.path.join(TEMPLATES_DIR, "cv.html"))

# 📌 Página de etiquetas -> etiqueta.html
@app.get("/etiqueta", response_class=HTMLResponse)
def etiqueta():
    return FileResponse(os.path.join(TEMPLATES_DIR, "etiqueta.html"))
