from comparador.ensamblador_prendas import EnsambladorPrendas

class AgenteEnsambladorPrendas:

    def __init__(self, estante_prendas):

        self.estante_prendas = estante_prendas
        self.ensamblador = EnsambladorPrendas()

    def trabajar(self, resumen):

        prendas = self.ensamblador.obtener_prendas(
            resumen
        )

        for clave, cantidad in prendas.items():

            self.estante_prendas.guardar({
                "clave": clave,
                "cantidad": cantidad
            })

        return prendas