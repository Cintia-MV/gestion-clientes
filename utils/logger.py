import logging

"""
Configuración del sistema de logs del proyecto.

Este módulo centraliza la configuración del logging
para toda la aplicación, permitiendo registrar eventos
importantes como:

- Creación de clientes
- Edición de datos
- Eliminación de clientes
- Errores de operación

Los logs se almacenan en el archivo:
    logs/app.log
"""

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("GIC")
