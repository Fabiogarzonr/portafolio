#!/usr/bin/env bash
set -e


PORT=${PORT:-8000}

echo "Iniciando aplicación en el puerto ${PORT}..."


exec uvicorn main:app --host 0.0.0.0 --port ${PORT}
