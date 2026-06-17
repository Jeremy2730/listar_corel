class EstanteConjuntos:

    def __init__(self):

        self.conjuntos = []

    def guardar(self, conjunto):

        self.conjuntos.append(conjunto)

    def obtener_todos(self):

        return self.conjuntos

    def total(self):

        return len(self.conjuntos)