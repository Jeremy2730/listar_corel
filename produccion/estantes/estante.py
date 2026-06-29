from copy import deepcopy


class Estante:

    def __init__(self):
        self._contenido = {}

    # =====================================
    # Agregar
    # =====================================

    def agregar(self, nombre, talla, cantidad=1):

        self._contenido.setdefault(nombre, {})
        self._contenido[nombre][talla] = (
            self._contenido[nombre].get(talla, 0) + cantidad
        )

    # =====================================
    # Consultar
    # =====================================

    def cantidad(self, nombre, talla):

        return (
            self._contenido
            .get(nombre, {})
            .get(talla, 0)
        )

    def existe(self, nombre, talla, cantidad=1):

        return self.cantidad(nombre, talla) >= cantidad

    def contiene(self, nombre):

        return nombre in self._contenido

    def tallas(self, nombre):

        return list(
            self._contenido
            .get(nombre, {})
            .keys()
        )

    def disponibles(self, nombre):

        return deepcopy(
            self._contenido.get(nombre, {})
        )

    # =====================================
    # Consumir
    # =====================================

    def consumir(self, nombre, talla, cantidad=1):

        if not self.existe(nombre, talla, cantidad):
            return False

        self._contenido[nombre][talla] -= cantidad

        if self._contenido[nombre][talla] == 0:
            del self._contenido[nombre][talla]

        if not self._contenido[nombre]:
            del self._contenido[nombre]

        return True

    # =====================================
    # Utilidades
    # =====================================

    def items(self):

        return self._contenido.items()

    def nombres(self):

        return list(self._contenido.keys())

    def total(self):

        total = 0

        for tallas in self._contenido.values():
            total += sum(tallas.values())

        return total

    def obtener_contenido(self):

        return deepcopy(self._contenido)

    def copiar(self):

        nuevo = self.__class__()
        nuevo._contenido = deepcopy(self._contenido)
        return nuevo

    def limpiar(self):

        self._contenido.clear()

    def vacio(self):

        return len(self._contenido) == 0

    # =====================================
    # Python
    # =====================================

    def __len__(self):

        return len(self._contenido)

    def __contains__(self, nombre):

        return nombre in self._contenido