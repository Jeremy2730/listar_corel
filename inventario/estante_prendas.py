# inventario/estante_prendas.py

class EstantePrendas:

    def __init__(self):

        self.prendas = []

    def guardar(self, prenda):

        self.prendas.append(prenda)

    def obtener_todas(self):

        return self.prendas

    def total(self):

        return len(self.prendas)