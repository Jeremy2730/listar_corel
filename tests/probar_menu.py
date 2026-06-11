from ui.menu import Menu
from pedidos.pedido_manager import PedidoManager

menu = Menu()
pedido_manager = PedidoManager()

opcion = menu.mostrar()

if opcion == "2":

    datos = pedido_manager.cargar()

    print(datos)

elif opcion == "3":

    if pedido_manager.eliminar():
        print("Pedido eliminado correctamente")
    else:
        print("No existe pedido")

elif opcion == "4":

    info = pedido_manager.obtener_info()

    print(info)