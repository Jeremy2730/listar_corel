# servicios/documento_actual.py

from servicios.corel_servicio import (
    obtener_corel
)

from servicios.analizador_documento import (
    analizar_documento
)

from reportes.encabezados import (
    mostrar_documento
)


def obtener_documento_actual():

    corel = obtener_corel()

    if not corel:
        return None

    nombre = corel.doc.Name

    mostrar_documento(
        nombre
    )

    analizador = analizar_documento(
        corel
    )

    return {
        "corel": corel,
        "nombre": nombre,
        "analizador": analizador
    }