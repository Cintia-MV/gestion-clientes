# Importar la clase base Cliente
from models.cliente import Cliente

# Definir la clase ClienteRegular
class ClienteRegular(Cliente):
    """
    Clase que representa a un cliente de tipo Regular.

    Hereda de la clase base Cliente y mantiene
    todos los atributos generales (id, nombre, email,
    telefono, direccion).

    Características:
    - No posee descuento (0%).
    - Permite conversión a diccionario para persistencia en JSON.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.descuento = 0           # Atributo específico del ClienteRegular

    # Método que convierte el objeto en diccionario
    def to_dict(self):
        data = super().to_dict()
        data["descuento"] = self.descuento
        return data
