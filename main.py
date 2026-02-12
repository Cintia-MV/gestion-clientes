from services.gestor_clientes import GestorClientes
from models.cliente_regular import ClienteRegular
from models.cliente_premium import ClientePremium
from models.cliente_corporativo import ClienteCorporativo
from utils.excepciones import DatosInvalidosError
from utils.entrada_usuario import (
    pedir_texto,
    pedir_email,
    pedir_telefono,
    pedir_texto_opcional
)

"""
Archivo principal del sistema Gestor Inteligente de Clientes (GIC).

Este módulo representa la capa de presentación (interfaz de usuario),
permitiendo la interacción mediante consola.

Responsabilidades:
- Mostrar el menú principal.
- Solicitar datos al usuario.
- Invocar las operaciones del GestorClientes.
- Manejar errores de validación.
"""

# Se instancia el gestor indicando la ruta del archivo JSON
gestor = GestorClientes("data/clientes.json")


# Funciones de vista (consola)
def separador():
    print("\n" + "*" * 50 + "\n")

#Muestra un título formateado en mayúsculas.
def titulo(texto):
    separador()
    print(texto.upper())
    separador()

#Muestra un mensaje de éxito destacado.
def mensaje_exito(texto):
    print("\n✅ " + texto + "\n")

#Muestra el mensaje inicial del sistema.
def bienvenida():
    titulo("Gestor Inteligente de Clientes (GIC)")
    print("Indicaciones:")
    print("- Email válido: ejemplo@dominio.com")
    print("- Teléfono: solo números, mínimo 8 dígitos")
    print("- No deje campos obligatorios vacíos")

#Muestra el menú principal de opciones.
def menu():
    separador()
    print("MENÚ PRINCIPAL")
    print("Seleccione una opción:\n")
    print("1. Crear cliente regular")
    print("2. Crear cliente premium")
    print("3. Crear cliente corporativo")
    print("4. Listar todos los clientes")
    print("5. Listar clientes por tipo")
    print("6. Editar cliente")
    print("7. Buscar cliente")
    print("8. Eliminar cliente")
    print("0. Salir")
    print()

# Programa principal
bienvenida()

while True:
    menu()
    opcion = input("Opción: ").strip()

    match opcion:
        # -------- CREAR CLIENTES --------
        case "1" | "2" | "3":
            titulo("Ingreso de nuevo cliente")

            try:
                datos = {
                    "nombre": pedir_texto("Nombre: "),
                    "email": pedir_email(),
                    "telefono": pedir_telefono(),
                    "direccion": pedir_texto("Dirección: ")
                }

                match opcion:
                    case "1":
                        cliente = ClienteRegular(**datos)
                    case "2":
                        cliente = ClientePremium(**datos)
                    case "3":
                        datos["empresa"] = pedir_texto("Empresa: ")
                        cliente = ClienteCorporativo(**datos)

                gestor.agregar_cliente(cliente)
                mensaje_exito("Cliente agregado correctamente")

            except DatosInvalidosError as e:
                print(f"Error: {e}")

        # -------- LISTAR TODOS --------
        case "4":
            titulo("Listado general de clientes")
            gestor.listar_clientes()

        # -------- LISTAR POR TIPO --------
        case "5":
            titulo("Listado de clientes por tipo")
            print("1. Cliente Regular")
            print("2. Cliente Premium")
            print("3. Cliente Corporativo")

            tipo = input("\nSeleccione tipo: ").strip()

            match tipo:
                case "1":
                    titulo("Listado de clientes regulares")
                    gestor.listar_clientes_por_tipo("ClienteRegular")
                case "2":
                    titulo("Listado de clientes premium")
                    gestor.listar_clientes_por_tipo("ClientePremium")
                case "3":
                    titulo("Listado de clientes corporativos")
                    gestor.listar_clientes_por_tipo("ClienteCorporativo")
                case _:
                    print("Tipo de cliente inválido")

        # -------- EDITAR --------
        case "6":
            titulo("Editar cliente")
            gestor.listar_clientes()

            try:
                indice = int(input("\nSeleccione el número del cliente a editar: "))
            except ValueError:
                print("Debe ingresar un número válido")
                continue

            print("\nDeje el campo vacío si no desea modificarlo\n")

            nuevos_datos = {
                "nombre": pedir_texto_opcional("Nuevo nombre: "),
                "email": pedir_texto_opcional("Nuevo email: "),
                "telefono": pedir_texto_opcional("Nuevo teléfono: "),
                "direccion": pedir_texto_opcional("Nueva dirección: ")
            }

            actualizado = gestor.editar_cliente_por_indice(indice, nuevos_datos)

            if actualizado:
                mensaje_exito("Cliente actualizado correctamente")
            else:
                print("Selección inválida")
        
        # -------- EDITAR --------
        case "7":
            titulo("Buscar cliente")

            print("Buscar por:")
            print("1. Email")
            print("2. Teléfono")

            opcion_busqueda = input("Seleccione opción: ").strip()

            if opcion_busqueda == "1":
                email = pedir_email()
                cliente = gestor.buscar_cliente(email=email)

            elif opcion_busqueda == "2":
                telefono = pedir_telefono()
                cliente = gestor.buscar_cliente(telefono=telefono)

            else:
                print("Opción inválida")
                continue

            if not cliente:
                print("No se encontró ningún cliente.")
            else:
                print("-" * 95)
                print(f"{'Nombre':<20} {'Email':<25} {'Teléfono':<15} {'Tipo':<20}")
                print("-" * 95)
                print(
                    f"{cliente['nombre']:<20} "
                    f"{cliente['email']:<25} "
                    f"{cliente['telefono']:<15} "
                    f"{cliente['tipo']:<20}"
                )
                print("-" * 95)

        # -------- ELIMINAR --------
        case "8":
            titulo("Eliminar cliente")
            gestor.listar_clientes()

            try:
                indice = int(input("\nSeleccione el número del cliente a eliminar: "))
            except ValueError:
                print("Debe ingresar un número válido")
                continue

            confirmacion = input(
                "\n¿Está seguro que desea eliminar este cliente? (s/n): "
            ).strip().lower()

            if confirmacion != "s":
                print("Operación cancelada")
                continue

            eliminado = gestor.eliminar_cliente_por_indice(indice)

            if eliminado:
                mensaje_exito("Cliente eliminado correctamente")
            else:
                print("Selección inválida")

        # -------- SALIR --------
        case "0":
            print("\nSaliendo de la aplicación...")
            print("...")
            print("Aplicación finalizada.\n")
            break

        # -------- OPCIÓN INVÁLIDA --------
        case _:
            print("Opción inválida. Intente nuevamente.")
