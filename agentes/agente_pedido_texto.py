class AgentePedidoTexto:

    def capturar(self):

        print("\n*** INGRESO PEDIDO ***\n")
        print("Ejemplos:")
        print("10 camisetas s")
        print("30 uniformes l")
        print("5 camisetas xl")
        print()
        print("Escriba OK para terminar.\n")

        lineas = []

        while True:

            texto = input("> ").strip()

            if texto.lower() == "ok":
                break

            if texto:
                lineas.append(texto)

        return lineas