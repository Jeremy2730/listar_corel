"""
Listar Corel

Objetivo:
Analizar automáticamente el documento abierto en CorelDRAW
y generar un resumen de piezas agrupadas por tamaño.

Funciones actuales:
- Conexión automática a CorelDRAW.
- Lectura de páginas y capas.
- Detección de objetos.
- Conversión de pulgadas a centímetros.
- Agrupación por medidas.
- Conteo automático de piezas.

Uso futuro:
- Detección de delanteros, espaldas y mangas.
- Clasificación por talla.
- Preparación para automatización de producción textil.
- Integración con el sistema de personalización de camisetas.
"""

from ui.menu import Menu
from pedidos.pedido_manager import PedidoManager
from pedidos.operaciones_listado import OperacionesListado

menu = Menu()

pedido_manager = PedidoManager()

operaciones_listado = OperacionesListado()

while True:

    opcion = menu.mostrar()

    if not opcion.isdigit():

        print(
            "\n⚠ Eso no es un número válido."
        )

        continue

    if opcion not in (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
    ):

        print(
            f"\n⚠ La opción {opcion} no existe."
        )

        continue

    if opcion == "1":

        operaciones_listado.crear_listado()

    elif opcion == "2":

        operaciones_listado.administrar_listado()

    elif opcion == "3":

        operaciones_listado.agregar_documento()

    elif opcion == "4":

        operaciones_listado.eliminar_listado()

    elif opcion == "5":

        operaciones_listado.listar_documento_actual()

    elif opcion == "6":

        print(
            "\nHasta luego. Gracias por usar Listar Corel."
        )

        break