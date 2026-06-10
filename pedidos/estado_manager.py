import json
from pathlib import Path


class EstadoManager:

    def __init__(self):

        self.archivo = Path(
            "datos/estado.json"
        )

    def guardar(self, datos):

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                datos,
                f,
                indent=4,
                ensure_ascii=False
            )

    def cargar(self):

        if not self.archivo.exists():

            return {
                "pedido_activo": False
            }

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)