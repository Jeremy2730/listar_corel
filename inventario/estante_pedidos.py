class EstantePedidos:

    def __init__(self):

        self.pedidos = []

    def guardar(self, pedido):

        self.pedidos.append(pedido)

    def obtener_todos(self):

        return self.pedidos