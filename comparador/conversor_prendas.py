from configuracion.orden_tallas import ORDEN_TALLAS


def obtener_prendas_producidas(acumulado):

    if not acumulado:
        return {}

    prendas = {}

    for talla in ORDEN_TALLAS:

        cantidad_camiseta = acumulado.get(
            f"camiseta {talla}",
            0
        )

        cantidad_manga = acumulado.get(
            f"manga {talla}",
            0
        )

        cantidad_pantaloneta = acumulado.get(
            f"pantaloneta {talla}",
            0
        )

        camisetas_por_cuerpo = (
            cantidad_camiseta // 2
        )

        camisetas_por_manga = (
            cantidad_manga // 2
        )

        camisetas = min(
            camisetas_por_cuerpo,
            camisetas_por_manga
        )

        pantalonetas = (
            cantidad_pantaloneta // 2
        )

        if camisetas > 0:

            prendas[
                f"camiseta {talla}"
            ] = camisetas

        if pantalonetas > 0:

            prendas[
                f"pantaloneta {talla}"
            ] = pantalonetas

    return prendas