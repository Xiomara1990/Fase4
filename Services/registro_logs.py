# Registro de eventos y errores del sistema

import logging
import os

# Crear la carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configuracion del registro de errores
logging.basicConfig(
    filename="logs/errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuracion del registro de eventos
eventos = logging.getLogger("eventos")
eventos.setLevel(logging.INFO)

if not eventos.handlers:
    archivo = logging.FileHandler("logs/eventos.log", encoding="utf-8")
    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    archivo.setFormatter(formato)
    eventos.addHandler(archivo)


def registrar_evento(mensaje):
    eventos.info(mensaje)


def registrar_error(mensaje):
    logging.error(mensaje)
