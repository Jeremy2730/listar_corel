from comparador.expandidor_pedido import ExpandidorPedido
from comparador.validacion_pedido import ValidadorPedido
from comparador.normalizador import Normalizador
from comparador.autocompletador import Autocompletador
from comparador.parser_pedido import ParserPedido


class ComparadorPedido:

    def __init__(self):
        self.validador = ValidadorPedido()
        self.parser = ParserPedido()
        self.normalizador = Normalizador()
        self.autocompletador = Autocompletador()


    def capturar_pedido_manual(self):

        pedido = {}

        print("\n===== INGRESO DE PEDIDO =====")
        print("Puedes escribir separado por comas:")
        print("Ej: 1 camiseta xl, 4 uniforme m, 3 uniforme s")
        print("Escribe 'OK' para terminar\n")

        while True:

            entrada = input(">> ").strip().lower()

            if entrada == "ok":
                break

            try:
                items = self.parser.parsear(entrada)

                if not items:
                    print("Entrada no reconocida")
                    continue

                for cantidad, prenda, talla in items:

                    prenda = self.autocompletador.completar(prenda)
                    prenda, talla = self.normalizador.normalizar(prenda, talla)
                    prenda = self.validador.validar_prenda(prenda)

                    if not prenda:
                        print(f"Ignorado: {cantidad} {prenda} {talla}")
                        continue

                    clave = f"{prenda} {talla}"
                    pedido[clave] = pedido.get(clave, 0) + cantidad

            except Exception:
                print("Error en formato")

        # 🔥 CONFIRMACIÓN FINAL
        if not self.confirmar_pedido(pedido):
            print("Pedido cancelado")
            return {}

        return pedido
    
    def confirmar_pedido(self, pedido):

        print("\n===== CONFIRMAR PEDIDO =====\n")

        for k, v in pedido.items():
            print(f"{v} x {k}")

        resp = input("\n¿Confirmar pedido? (S/N): ").strip().upper()

        return resp == "S"


    def obtener_claves_ordenadas(self, pedido_expandido, produccion):

        claves = set(pedido_expandido.keys()) | set(produccion.keys())

        return sorted(list(claves))
    

    def comparar_pedido(self, pedido, produccion):

        expandidor = ExpandidorPedido()
        pedido_expandido = ExpandidorPedido().expandir(pedido)

        produccion_expandida = produccion

        resultado = []

        faltantes_totales = 0
        sobrantes_totales = 0

        claves = sorted(
            self.obtener_claves_ordenadas(pedido_expandido, produccion),
            key=lambda x: (x.split(" ")[0], x.split(" ")[1] if len(x.split(" ")) > 1 else "")
        )

        for clave in claves:

            solicitado = pedido_expandido.get(clave, 0)

            producido = produccion.get(clave, 0)

            if solicitado == 0 and producido == 0:
                continue

            diferencia = producido - solicitado

            if diferencia == 0:
                estado = "COMPLETO"

            elif diferencia > 0:
                estado = f"SOBRAN {diferencia}"
                sobrantes_totales += diferencia

            else:
                estado = f"FALTAN {abs(diferencia)}"
                faltantes_totales += abs(diferencia)

            resultado.append({

                "prenda": clave,
                "pedido": solicitado,
                "producido": producido,
                "estado": estado

            })

        return resultado, faltantes_totales, sobrantes_totales


    def mostrar_comparacion(
        self,
        resultado,
        faltantes,
        sobrantes
    ):

        print("\n" + "=" * 60)
        print("COMPARACION DE PEDIDO")
        print("=" * 60)

        for fila in resultado:

            print(
                f"{fila['prenda']:<25}"
                f"Pedido:{fila['pedido']:>4}   "
                f"Prod:{fila['producido']:>4}   "
                f"{fila['estado']}"
            )

        print("=" * 60)
        print(f"Faltantes totales : {faltantes}")
        print(f"Sobrantes totales : {sobrantes}")


