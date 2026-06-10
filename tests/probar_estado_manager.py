from pedidos.estado_manager import EstadoManager


estado = EstadoManager()

print("\nGuardando estado...")

estado.guardar(
    {
        "pedido_activo": True
    }
)

print("\nLeyendo estado...")

datos = estado.cargar()

print(datos)