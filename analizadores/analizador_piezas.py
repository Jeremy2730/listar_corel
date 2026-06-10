from collections import defaultdict
from catalogos.catalogo_buscador import BuscadorCatalogo

class AnalizadorPiezas:

    PULGADA_A_CM = 2.54

    def __init__(self):

        self.conteo = defaultdict(int)
        self.no_reconocidos = defaultdict(int)
        self.buscador = BuscadorCatalogo()

    def analizar(self, shape):

        try:

            ancho = round(
                shape.SizeWidth * self.PULGADA_A_CM,
                1
            )

            alto = round(
                shape.SizeHeight * self.PULGADA_A_CM,
                1
            )

            if ancho < 1 or alto < 1:
                return

            medidas = sorted([ancho, alto])

            resultado = self.buscador.buscar(
                medidas[0],
                medidas[1]
            )

            if resultado:

                clave = (
                    f"{resultado['producto']} "
                    f"{resultado['talla']}"
                )

                self.conteo[clave] += 1

            else:

                clave = (
                    f"{self.formatear(medidas[0])} x "
                    f"{self.formatear(medidas[1])} cm"
                )

                self.no_reconocidos[clave] += 1

        except Exception as e:

            print("Error:", e)


    def mostrar_resumen(self):

        print("\n===== RECONOCIDOS =====\n")

        for clave, cantidad in sorted(self.conteo.items()):

            print(f"{clave} -> {cantidad} piezas")

        print("\n===== NO RECONOCIDOS =====\n")

        for clave, cantidad in sorted(self.no_reconocidos.items()):

            print(f"{clave} -> {cantidad} piezas")


    def formatear(self, valor):

        if valor.is_integer():
            return str(int(valor))

        return str(valor)


    def obtener_resumen(self):

        return dict(self.conteo)
    
    def total_piezas(self):

        return sum(self.conteo.values())
    
    def total_no_reconocidos(self):

        return sum(self.no_reconocidos.values())
    
    def obtener_no_reconocidos(self):

        return dict(self.no_reconocidos)