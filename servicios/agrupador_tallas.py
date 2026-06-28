# servicios/agrupador_tallas.py

def agrupar_por_tallas(datos):

    agrupado = {}

    for clave, cantidad in datos.items():

        producto, talla = clave.rsplit(
            " ",
            1
        )

        agrupado.setdefault(
            talla,
            {}
        )[producto] = cantidad

    return agrupado