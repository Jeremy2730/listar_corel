from produccion.recetas.recetas_prendas import RECETAS_PRENDAS
from produccion.recetas.recetas_conjuntos import RECETAS_CONJUNTOS


class LibroRecetas:

    def __init__(self):

        self._prendas = RECETAS_PRENDAS
        self._conjuntos = RECETAS_CONJUNTOS


    def obtener(self, nombre):

        if nombre in self._prendas:
            return self._prendas[nombre]

        if nombre in self._conjuntos:
            return self._conjuntos[nombre]

        return None


    def existe_prenda(self, nombre):

        return nombre in self._prendas


    def existe_conjunto(self, nombre):

        return nombre in self._conjuntos


    def listar_prendas(self):

        return list(self._prendas.keys())


    def listar_conjuntos(self):

        return list(self._conjuntos.keys())