from configuracion.orden_tallas import ORDEN_TALLAS
from comparador.configuracion_prendas import PRENDAS


class EnsambladorPrendas:

    def obtener_prendas(self, resumen):

        prendas = {}

        for talla in ORDEN_TALLAS:

            for nombre_prenda, piezas in PRENDAS.items():

                cantidades = []

                for pieza in piezas:

                    cantidades.append(
                        resumen.get(
                            f"{pieza} {talla}",
                            0
                        )
                    )

                ensambladas = min(cantidades)

                if ensambladas > 0:

                    prendas[
                        f"{nombre_prenda} {talla}"
                    ] = ensambladas

        return prendas


    def obtener_piezas_prenda(
        self,
        resumen,
        talla,
        nombre_prenda
    ):

        piezas = {}

        for pieza in PRENDAS[nombre_prenda]:

            piezas[pieza] = resumen.get(
                f"{pieza} {talla}",
                0
            )

        return piezas

    def obtener_incompletos(self, resumen):

        incompletos = []

        for talla in ORDEN_TALLAS:

            for nombre_prenda in PRENDAS:

                piezas = self.obtener_piezas_prenda(
                    resumen,
                    talla,
                    nombre_prenda
                )

                cantidades = list(
                    piezas.values()
                )

                maximo = max(cantidades)

                if maximo == 0:
                    continue

                ensambladas = min(cantidades)

                if ensambladas < maximo:

                    incompletos.append({

                        "prenda": nombre_prenda,

                        "talla": talla,

                        "piezas": piezas

                    })

        return incompletos