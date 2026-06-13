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
from pedidos.operaciones_listado import OperacionesListado

menu = Menu()

pedido_manager = PedidoManager()

operaciones_listado = OperacionesListado()

estado_manager = EstadoManager()

opcion = menu.mostrar()


if opcion == "1":

    nombre_listado = input(
        "\nNombre del listado: "
    )

    corel = CorelAPI()

    if not corel.conectar():
        exit()
    print()
    print("DOCUMENTO:")
    print(corel.doc.Name)
    print()

    nombre_documento = corel.doc.Name

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
        "nombre": nombre_listado,
        "fecha": str(date.today()),

        "documentos": [
            {
                "archivo": nombre_documento,
                "resumen": analizador.obtener_resumen()
            }
        ],

        "acumulado": analizador.obtener_resumen()
    }

    pedido_manager.guardar(
        datos_pedido
    )

    estado_manager.marcar_pedido_activo()

    print(
        "\nPedido guardado correctamente."
    )


if opcion == "2":

    operaciones_listado.ver_listado()

    exit()

if opcion == "3":

    pedido = pedido_manager.cargar()

    if not pedido:

        print(
            "No existe listado activo."
        )

        exit()

    corel = CorelAPI()

    if not corel.conectar():
        exit()

    nombre_documento = corel.doc.Name

    print()
    print("DOCUMENTO:")
    print(nombre_documento)
    print()

    for doc in pedido["documentos"]:

        if doc["archivo"] == nombre_documento:

            print(
                "Ese documento ya fue agregado."
            )

            exit()

    analizador = AnalizadorPiezas()

    for shape in corel.obtener_shapes():

        analizador.analizar(shape)

    resumen = ResumenProduccion(
        analizador.obtener_resumen(),
        analizador.obtener_no_reconocidos()
    )

    resumen.mostrar()

    respuesta = input(
        "\nAgregar documento al listado? (s/n): "
    )

    if respuesta.lower() != "s":

        print(
            "Operacion cancelada."
        )

        exit()

    nuevo_documento = {

        "archivo": nombre_documento,

        "resumen": analizador.obtener_resumen()
    }

    pedido["documentos"].append(
        nuevo_documento
    )

    for clave, cantidad in (
        analizador.obtener_resumen().items()
    ):

        pedido["acumulado"][clave] = (

            pedido["acumulado"].get(
                clave,
                0
            )

            + cantidad
        )

    pedido_manager.guardar(
        pedido
    )

    print(
        "\nDocumento agregado correctamente."
    )

    exit()


if opcion == "4":

    operaciones_listado.eliminar_listado()

    exit()


if opcion == "5":

    operaciones_listado.listar_documento_actual()

    exit()