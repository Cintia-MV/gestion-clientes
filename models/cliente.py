import uuid
from utils.validaciones import validar_email, validar_telefono
from utils.excepciones import DatosInvalidosError

class Cliente:
    """
    Clase base que representa un cliente dentro del sistema.

    Esta clase contiene los atributos comunes a todos los tipos de clientes:
    - id (generado automáticamente con UUID)
    - nombre
    - email
    - telefono
    - direccion

    Además, incluye validaciones internas para asegurar la integridad
    de los datos y métodos especiales para representación y comparación.
    """
    # Inicializa un objeto Cliente.
    def __init__(self, **kwargs):
        # Genera un identificador único para cada cliente
        self.id = str(uuid.uuid4())
        # Asignación de atributos recibidos mediante kwargs
        self.nombre = kwargs.get("nombre")
        self.email = kwargs.get("email")
        self.telefono = kwargs.get("telefono")
        self.direccion = kwargs.get("direccion")
        # Validación automática de los datos ingresados
        self._validar_datos()

    #Método interno que valida los datos del cliente.
    def _validar_datos(self):
        if not self.nombre:
            raise DatosInvalidosError("El nombre es obligatorio")

        if not validar_email(self.email):
            raise DatosInvalidosError("Email inválido")

        if not validar_telefono(self.telefono):
            raise DatosInvalidosError("Teléfono inválido")

    #Convierte el objeto Cliente en un diccionario.
    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion
        }

    #Devuelve una representación legible del cliente.
    def __str__(self):
        return f"{self.nombre} ({self.email})"

    #Permite comparar dos clientes.
    def __eq__(self, other):
        return self.id == other.id
