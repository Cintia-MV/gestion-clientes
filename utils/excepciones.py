class DatosInvalidosError(Exception):
    """
    Excepción personalizada para indicar que los datos
    ingresados no cumplen con las validaciones requeridas.

    Esta clase hereda de la clase base Exception.

    Uso:
        Se lanza cuando:
        - El nombre está vacío.
        - El email no tiene formato válido.
        - El teléfono no cumple con las reglas establecidas.
    """
    pass
