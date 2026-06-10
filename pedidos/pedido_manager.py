import json
from pathlib import Path


class PedidoManager:

    def __init__(self):

        self.archivo = Path("datos/pedido_base.json")

    def existe(self):

        return self.archivo.exists()

    def guardar(self, datos):

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar(self):

        if not self.existe():
            return None

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    def eliminar(self):

        if self.existe():

            self.archivo.unlink()

            return True

        return False

    def obtener_info(self):

        datos = self.cargar()

        if not datos:
            return None

        return {
            "nombre": datos.get("nombre", ""),
            "fecha": datos.get("fecha", ""),
            "total_piezas": datos.get("total_piezas", 0)
        }