from pedidos.estado_manager import EstadoManager

estado = EstadoManager()

print("Archivo:", estado.archivo.resolve())

datos = estado.cargar()

print("Datos:", datos)

if datos["pedido_activo"]:

    print(
        "Hay un pedido guardado."
    )

else:

    print(
        "No hay pedidos guardados."
    )