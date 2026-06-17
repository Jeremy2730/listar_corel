from comparador.ensamblador_conjuntos import (
    EnsambladorConjuntos
)

class AgenteEnsambladorConjuntos:

    def __init__(self, estante_conjuntos):

        self.estante_conjuntos = (
            estante_conjuntos
        )

        self.ensamblador = (
            EnsambladorConjuntos()
        )

    def trabajar(self, prendas):

        conjuntos = (
            self.ensamblador.obtener_conjuntos(
                prendas
            )
        )

        for clave, cantidad in conjuntos.items():

            self.estante_conjuntos.guardar({

                "clave": clave,
                "cantidad": cantidad
            })

        return conjuntos