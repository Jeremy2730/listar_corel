import win32com.client


class CorelAPI:

    def __init__(self):
        self.app = None
        self.doc = None

    def conectar(self):

        for v in range(15, 30):

            try:

                self.app = win32com.client.Dispatch(
                    f"CorelDRAW.Application.{v}"
                )

                self.doc = self.app.ActiveDocument

                if self.doc is None:

                    print(
                        "Corel esta abierto pero no hay documento abierto."
                    )

                    return False

                print(f"Conectado a Corel v{v}")

                return True

            except Exception as e:

                mensaje = str(e)

                if "Cadena clase no válida" in mensaje:
                    continue

                raise

        print("No se encontro CorelDRAW abierto.")

        return False

    def obtener_shapes(self):

        if self.doc is None:
            return

        for page in self.doc.Pages:

            for layer in page.Layers:

                for i in range(
                    1,
                    layer.Shapes.Count + 1
                ):

                    yield layer.Shapes.Item(i)