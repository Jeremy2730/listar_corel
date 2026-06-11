from pedidos.estado_manager import EstadoManager

estado = EstadoManager()

estado.marcar_pedido_activo()

print(estado.cargar())