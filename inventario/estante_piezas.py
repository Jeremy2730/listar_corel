class EstantePiezas:

    def __init__(self):

        self.piezas = []

    def guardar(self, pieza):

        self.piezas.append(pieza)

    def obtener_todas(self):

        return self.piezas

    def total_piezas(self):

        return len(self.piezas)