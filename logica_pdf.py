# logica_pdf_tesseract.py
import re
import fitz  # PyMuPDF
import json
import os
from langdetect import detect
from translate import Translator
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

from h_p_ordenada import h_p_data_ordenada
from frases_p_ordenada import frases_p_statements_ordenadas
from h_p_list import h_p_data_list
from h_p_lista import h_p_data_lista

# ===============================
# CONFIGURACIÓN
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "h_code_pictogram_map.json"), "r", encoding="utf-8") as f:
    h_code_map = json.load(f)

translator = Translator(to_lang="es")

# ===============================
# FUNCIONES AUXILIARES
# ===============================

def extract_text_from_pdf(pdf_path):
    """Extrae texto de PDF. Si no tiene texto, usa OCR con Tesseract."""
    text = ""
    doc = fitz.open(pdf_path)

    # Intentar primero con PyMuPDF (texto embebido)
    for page in doc:
        page_text = page.get_text()
        if page_text:
            text += page_text

    # Si no encontró texto, hacer OCR
    if not text.strip():
        text = extract_text_with_ocr(pdf_path)

    return text

def extract_text_with_ocr(pdf_path):
    """Extrae texto de PDF usando OCR con Tesseract."""
    text = ""
    images = convert_from_path(pdf_path, dpi=300)
    for img in images:
        ocr_text = pytesseract.image_to_string(img, lang="spa+eng")
        text += ocr_text + "\n"
    return text

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def translate_text(text):
    try:
        return translator.translate(text)
    except:
        return text

def extract_h_p_indicators(text):
    """Busca frases H y P en el texto."""
    pattern = r"(H\d{3}[A-Za-z]{0,2}|P\d{3}[A-Za-z]{0,2})\s+([^\.]+?\.)"
    matches = re.findall(pattern, text, re.DOTALL)
    unique_matches = list({tag: description for tag, description in matches}.items())
    return unique_matches

def seleccionar_importantes(h_p_data, max_items=3):
    """Selecciona frases H y P más relevantes según la lista priorizada."""
    h_tags = [tag for tag, _ in h_p_data if tag.startswith("H")]
    p_tags = [tag for tag, _ in h_p_data if tag.startswith("P")]

    h_prioritized = sorted(
        [item for item in h_p_data_ordenada if item[0] in h_tags],
        key=lambda x: x[2]
    )[:max_items]

    p_prioritized = sorted(
        [item for item in frases_p_statements_ordenadas if item[0] in p_tags],
        key=lambda x: x[2]
    )[:max_items]

    final_data = [(tag, desc) for tag, desc, _ in h_prioritized + p_prioritized]
    return final_data[:max_items]

def detectar_pictogramas_por_texto(text):
    """Detecta pictogramas solo por presencia de H-codes en el texto."""
    detected_ghs = set()
    pattern = re.compile(r"H\d{3}")
    matches = pattern.findall(text)

    for h_code in matches:
        pictos = h_code_map.get(h_code)
        if pictos:
            detected_ghs.update(pictos)

    if "NoAplica" in detected_ghs and len(detected_ghs) > 1:
        detected_ghs.discard("NoAplica")

    return list(detected_ghs)

# ===============================
# FUNCIÓN PRINCIPAL
# ===============================

def procesar_pdfs(lista_pdfs):
    frases_total = []
    pictos_total = []

    for pdf in lista_pdfs:
        texto = extract_text_from_pdf(pdf)
        idioma = detect_language(texto)

        h_p_data = extract_h_p_indicators(texto)
        if not h_p_data:
            if idioma == "en":
                h_p_data = [(tag, desc) for tag, desc in h_p_data_list if desc in texto]
            elif idioma == "es":
                h_p_data = [(tag, desc) for tag, desc in h_p_data_lista if desc in texto]

        if idioma == "en":
            h_p_data = [(tag, translate_text(desc)) for tag, desc in h_p_data]

        frases_total.extend(h_p_data)
        pictos_total.extend(detectar_pictogramas_por_texto(texto))

    frases_unicas = {tag: desc for tag, desc in frases_total}
    frases_finales = seleccionar_importantes(list(frases_unicas.items()), max_items=3)

    PICTO_PRIORITY = {
         "GHS01": 1,
         "GHS02": 1,
         "GHS03": 1,
         "GHS04": 1,

         "GHS06": 2,
         "GHS08": 2,
         "GHS05": 2,

         "GHS07": 3,

         "GHS09": 4
    }


    pictos_unicos = list(set(pictos_total))


    pictos_ordenados = sorted(
        pictos_unicos,
        key=lambda x: PICTO_PRIORITY.get(x, 99)
    )


    pictos_finales = pictos_ordenados[:2]



    return {
        "frases": [f"{tag}: {desc}" for tag, desc in frases_finales],
        "pictogramas": pictos_finales
    }
