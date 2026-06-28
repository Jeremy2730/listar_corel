# pedidos/fabrica_documento.py

def crear_documento(
    nombre,
    analizador
):

    return {

        "archivo": nombre,

        "resumen": (
            analizador.obtener_resumen()
        ),

        "no_reconocidos": (
            analizador.obtener_no_reconocidos()
        )
    }