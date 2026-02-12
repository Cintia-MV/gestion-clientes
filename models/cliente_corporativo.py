# Importar la clase base Cliente
from models.cliente import Cliente


class ClienteCorporativo(Cliente):

    """
    Clase que representa a un cliente de tipo Corporativo.

    Extiende la clase Cliente agregando el atributo 'empresa',
    que identifica la organización asociada al cliente.
    """
    def __init__(self, **kwargs):
        # Llamar al constructor de la clase padre (Cliente)
        super().__init__(**kwargs)
        self.empresa = kwargs.get("empresa") # Agregar el atributo específico de esta clase

    # Método que convierte el objeto en diccionario
    def to_dict(self):
        data = super().to_dict()
        data["empresa"] = self.empresa # Agregar al diccionario el atributo específico de ClienteCorporativo
        return data
