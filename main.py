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


from corel.corel_api import CorelAPI
from analizadores.analizador_piezas import AnalizadorPiezas
from pedidos.resumen_produccion import ResumenProduccion
from ui.menu import Menu
from pedidos.pedido_manager import PedidoManager
from pedidos.estado_manager import EstadoManager
from datetime import date

menu = Menu()

pedido_manager = PedidoManager()

estado_manager = EstadoManager()

opcion = menu.mostrar()


if opcion == "1":

    corel = CorelAPI()

    if not corel.conectar():
        exit()
    print()
    print("DOCUMENTO:")
    print(corel.doc.Name)
    print()

    analizador = AnalizadorPiezas()
    
    for shape in corel.obtener_shapes():
        analizador.analizar(shape)

    resumen = ResumenProduccion(
        analizador.obtener_resumen(),
        analizador.obtener_no_reconocidos()
    )

    resumen.mostrar()

    print()

    datos_pedido = {
        "nombre": "Pedido Base",
        "fecha": str(date.today()),
        "total_piezas": sum(
            analizador.obtener_resumen().values()
        ),
        "resumen": analizador.obtener_resumen()
    }

    pedido_manager.guardar(
        datos_pedido
    )

    estado_manager.marcar_pedido_activo()

    print(
        "\nPedido guardado correctamente."
    )


if opcion == "2":

    pedido = pedido_manager.cargar()

    if not pedido:

        print("No existe pedido guardado.")
        exit()

    print("\n===== PEDIDO ACTIVO =====\n")

    print(f"Nombre: {pedido['nombre']}")
    print(f"Fecha: {pedido['fecha']}")
    print(f"Total piezas: {pedido['total_piezas']}")

    resumen = ResumenProduccion(
        pedido["resumen"]
    )

    resumen.mostrar()

    exit()


if opcion == "3":

    if pedido_manager.eliminar():

        estado_manager.marcar_sin_pedido()

        print(
            "Pedido eliminado."
        )

    else:

        print(
            "No existe pedido."
        )

    exit()