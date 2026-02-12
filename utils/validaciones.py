import re

def validar_email(email):
    """
    Valida el formato de un correo electrónico.
        - Se utiliza una expresión regular (regex) para verificar
        que el email tenga estructura básica:
            texto@dominio.extension
        - No valida existencia real del correo, solo su formato.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email)

def validar_telefono(telefono):
    """
    Valida un número de teléfono.
        - Debe contener únicamente caracteres numéricos.
        - Debe tener una longitud mínima de 8 dígitos.
    """
    return telefono.isdigit() and len(telefono) >= 8
