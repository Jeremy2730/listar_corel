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

            ancho = shape.SizeWidth * self.PULGADA_A_CM
            alto = shape.SizeHeight * self.PULGADA_A_CM

            ancho = round(ancho, 1)
            alto = round(alto, 1)

            if ancho < 1 or alto < 1:
                return

            medidas = sorted([ancho, alto])
            nombre_shape = shape.Name.strip().lower()

            resultado = self.buscador.buscar(
                medidas[0],
                medidas[1],
                nombre_shape
            )

            if resultado:

                clave = (
                    f"{resultado['pieza']} "
                    f"{resultado['talla']}"
                )

                self.conteo[clave] += 1

            else:

                if nombre_shape:

                    clave = (
                        f"{nombre_shape} | "
                        f"{self.formatear(medidas[0])} x "
                        f"{self.formatear(medidas[1])} cm"
                    )

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

        if valor == int(valor):
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