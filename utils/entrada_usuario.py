from utils.validaciones import validar_email, validar_telefono

def pedir_texto(mensaje):
    """
    Solicita al usuario un texto obligatorio.

    Args:
        mensaje (str): Mensaje que se mostrará en consola.

    Returns:
        str: Texto ingresado por el usuario.

    Comportamiento:
        - Repite la solicitud hasta que el usuario
        ingrese un valor no vacío.
    """
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("⚠️  Este campo no puede estar vacío.")

def pedir_email():
    """
    Solicita al usuario un email válido.

    Returns:
        str: Email validado.

    Comportamiento:
        - Valida el formato usando la función validar_email.
        - Repite la solicitud hasta que el email sea correcto.
    """
    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            return email
        print("⚠️  Email inválido. Ejemplo: usuario@dominio.com")

def pedir_telefono():
    """
    Solicita al usuario un número de teléfono válido.

    Returns:
        str: Teléfono validado.

    Comportamiento:
        - Solo permite números.
        - Debe tener al menos 8 dígitos.
        - Repite la solicitud hasta que el dato sea válido.
    """
    while True:
        telefono = input("Teléfono: ").strip()
        if validar_telefono(telefono):
            return telefono
        print("⚠️  Teléfono inválido. Use solo números (mín. 8 dígitos)")

def pedir_texto_opcional(mensaje):
    valor = input(mensaje).strip()
    return valor if valor else None

