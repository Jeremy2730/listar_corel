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
        
    def hay_pedido_activo(self):

        datos = self.cargar()

        return datos.get(
            "pedido_activo",
            False
        )


    def marcar_pedido_activo(self):

        self.guardar(
            {
                "pedido_activo": True
            }
        )


    def marcar_sin_pedido(self):

        self.guardar(
            {
                "pedido_activo": False
            }
        )