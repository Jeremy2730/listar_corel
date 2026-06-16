class Pieza:

    def __init__(self, shape=None):

        # Corel
        self.shape = shape
        self.layer = getattr(shape, "Layer", "")
        self.page = getattr(shape, "PageIndex", 0)

        # Medidas
        self.ancho = 0.0
        self.alto = 0.0

        # Identidad
        self.nombre = getattr(shape, "Name", "") or ""

        # Clasificación
        self.reconocida = False
        self.clave = None

        # Producción
        self.cantidad = 1

        # Resultado catálogo
        self.producto = None
        self.pieza = None
        self.talla = None