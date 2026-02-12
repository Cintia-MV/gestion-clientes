import json

def guardar_clientes(ruta, clientes):
    """
    Guarda la lista de clientes en un archivo JSON.

    Args:
        ruta (str): Ruta del archivo donde se almacenarán los datos.
        clientes (list): Lista de clientes en formato diccionario.

    Funcionalidad:
        - Abre el archivo en modo escritura.
        - Convierte la lista de clientes en formato JSON.
        - Utiliza indentación para mejorar la legibilidad.
        - Mantiene caracteres especiales (acentos, ñ, etc.).
    """
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def cargar_clientes(ruta):
    """
    Carga los clientes desde un archivo JSON.

    Args:
        ruta (str): Ruta del archivo JSON.

    Returns:
        list: Lista de clientes en formato diccionario.
            Si el archivo no existe, retorna una lista vacía.

    Manejo de errores:
        - Si el archivo no existe, se captura la excepción
        FileNotFoundError y se retorna una lista vacía.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
