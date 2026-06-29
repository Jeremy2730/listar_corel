from produccion.estantes.estante_piezas import EstantePiezas
from produccion.estantes.estante_prendas import EstantePrendas
from produccion.estantes.estante_produccion import EstanteProduccion


class FabricaEstantes:

    def crear_estante_piezas(self, acumulado):

        estante = EstantePiezas()

        for nombre, tallas in acumulado.items():

            for talla, cantidad in tallas.items():

                estante.agregar(
                    nombre,
                    talla,
                    cantidad
                )

        return estante


    def crear_estante_prendas(self):

        return EstantePrendas()


    def crear_estante_produccion(self):

        return EstanteProduccion()