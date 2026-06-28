from catalogos.camisetas import CATALOGO_CAMISETAS
from catalogos.mangas import CATALOGO_MANGAS
from catalogos.mangas_largas import CATALOGO_MANGAS_LARGAS
from catalogos.pantalonetas import CATALOGO_PANTALONETAS

MODO_ESTRICTO = True

class BuscadorCatalogo:

    def __init__(self):

        self.catalogos = {
            "camiseta": CATALOGO_CAMISETAS,
            "manga": CATALOGO_MANGAS,
            "manga_larga": CATALOGO_MANGAS_LARGAS,
            "pantaloneta": CATALOGO_PANTALONETAS
        }


    def limpiar(self, valor):
        if isinstance(valor, tuple):
            return valor[0]
        return valor

    def buscar(
        self,
        ancho,
        alto,
        nombre_shape
    ):

        nombre_shape = (
            nombre_shape
            .lower()
            .strip()
            .replace("_", " ")
            .replace("-", " ")
        )

        if MODO_ESTRICTO and not nombre_shape:
            return None

        ancho = self.limpiar(ancho)
        alto = self.limpiar(alto)

        ancho = round(ancho, 1)
        alto = round(alto, 1)

        medidas_shape = sorted([ancho, alto])

        mejor_match = None
        menor_error = float("inf")
        coincidencia_nombre = False

        for producto, catalogo in self.catalogos.items():

            for talla, piezas in catalogo.items():

                for pieza, datos in piezas.items():

                    pieza_normalizada = (
                        pieza.lower()
                        .strip()
                        .replace("_", " ")
                        .replace("-", " ")
                    )

                    if nombre_shape != pieza_normalizada:
                        continue

                    coincidencia_nombre = True

                    medidas_catalogo = sorted([
                        round(datos["ancho"], 1),
                        round(datos["alto"], 1)
                    ])

                    porc_ancho = abs(medidas_shape[0] - medidas_catalogo[0]) / medidas_catalogo[0]
                    porc_alto = abs(medidas_shape[1] - medidas_catalogo[1]) / medidas_catalogo[1]

                    error = (porc_ancho + porc_alto) * 100

                    if error < menor_error:
                        menor_error = error

                        mejor_match = {
                            "producto": producto,
                            "talla": talla,
                            "pieza": pieza
                        }
        
        if not coincidencia_nombre:
            return None

        if menor_error > 6:
            return None

        return mejor_match