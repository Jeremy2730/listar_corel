from pedidos.estado_manager import EstadoManager

estado = EstadoManager()

estado.guardar(
    {
        "pedido_activo": False
    }
)

print(estado.cargar())