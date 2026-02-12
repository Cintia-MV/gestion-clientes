# Importar la clase base Cliente
from models.cliente import Cliente


class ClientePremium(Cliente):
    """
    Clase que representa a un cliente de tipo Premium.

    Hereda de Cliente y agrega un beneficio adicional:
    un descuento fijo del 20%.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.descuento = 20         # Atributo específico de ClientePremium

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        data = super().to_dict()
        data["descuento"] = self.descuento # Agrega el atributo específico de ClientePremium
        return data
