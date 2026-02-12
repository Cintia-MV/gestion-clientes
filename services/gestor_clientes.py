from utils.archivo_json import guardar_clientes, cargar_clientes
from utils.logger import logger

class GestorClientes:
    """
    Clase encargada de gestionar la lógica de negocio
    relacionada con los clientes.

    Responsabilidades:
    - Cargar clientes desde archivo JSON.
    - Agregar nuevos clientes.
    - Listar clientes.
    - Filtrar clientes por tipo.
    - Editar clientes.
    - Eliminar clientes.
    - Registrar eventos en logs operacionales.

    Esta clase actúa como capa de servicio dentro de la arquitectura.
    """
    #Inicializa el gestor de clientes.
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        self.clientes = cargar_clientes(self.ruta)

    # Agrega un nuevo cliente al sistema
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente.to_dict())
        guardar_clientes(self.ruta, self.clientes)

        #Registra la acción en el log.
        logger.info(
        f"Cliente creado | Tipo: {cliente.__class__.__name__} | ID: {cliente.id}"
        )

    #Muestra en consola todos los clientes registrados
    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("-" * 95)
        print(f"{'N°':<5} {'Nombre':<20} {'Email':<25} {'Teléfono':<15} {'Tipo':<20}")
        print("-" * 95)

        for i, cliente in enumerate(self.clientes, start=1):
            print(
                f"{i:<5} "
                f"{cliente['nombre']:<20} "
                f"{cliente['email']:<25} "
                f"{cliente['telefono']:<15} "
                f"{cliente['tipo']:<20}"
            )

        print("-" * 95)

    #Muestra en consola los clientes filtrados por tipo.
    def listar_clientes_por_tipo(self, tipo):
        filtrados = [c for c in self.clientes if c["tipo"] == tipo]

        if not filtrados:
            print("No hay clientes de este tipo.")
            return

        print("-" * 95)
        print(f"{'N°':<5} {'Nombre':<20} {'Email':<25} {'Teléfono':<15}")
        print("-" * 95)

        for i, cliente in enumerate(filtrados, start=1):
            print(
                f"{i:<5} "
                f"{cliente['nombre']:<20} "
                f"{cliente['email']:<25} "
                f"{cliente['telefono']:<15}"
            )

        print("-" * 95)

    #Edita un cliente existente según su posición en la lista.
    def editar_cliente_por_indice(self, indice, nuevos_datos):
        try:
            cliente = self.clientes[indice - 1]

            for clave, valor in nuevos_datos.items():
                if valor:
                    cliente[clave] = valor

            guardar_clientes(self.ruta, self.clientes)
            
            logger.info(
            f"Cliente editado | ID: {cliente['id']}"
            )
            return True

        except IndexError:
            logger.error(
                f"Intento de edición con índice inválido: {indice}"
        )
        return False
    
    #Buscar un cliente por email o teléfono.
    def buscar_cliente(self, email=None, telefono=None):
        for cliente in self.clientes:
            if email and cliente["email"] == email:
                return cliente
            if telefono and cliente["telefono"] == telefono:
                return cliente

        return None

    #Elimina un cliente según su posición en la lista.
    def eliminar_cliente_por_indice(self, indice):
        try:
            cliente = self.clientes.pop(indice - 1)
            guardar_clientes(self.ruta, self.clientes)

            logger.info(
                f"Cliente eliminado | ID: {cliente['id']}"
            )
            return True

        except IndexError:
            logger.error(
                f"Intento de eliminación con índice inválido: {indice}"
            )
            return False


