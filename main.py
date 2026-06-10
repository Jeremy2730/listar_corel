"""
Listar Corel

Objetivo:
Analizar automáticamente el documento abierto en CorelDRAW
y generar un resumen de piezas agrupadas por tamaño.

Funciones actuales:
- Conexión automática a CorelDRAW.
- Lectura de páginas y capas.
- Detección de objetos.
- Conversión de pulgadas a centímetros.
- Agrupación por medidas.
- Conteo automático de piezas.

Uso futuro:
- Detección de delanteros, espaldas y mangas.
- Clasificación por talla.
- Preparación para automatización de producción textil.
- Integración con el sistema de personalización de camisetas.
"""


from corel.corel_api import CorelAPI
from analizadores.analizador_piezas import AnalizadorPiezas
from pedidos.resumen_produccion import ResumenProduccion


corel = CorelAPI()

if not corel.conectar():
    exit()

analizador = AnalizadorPiezas()

for shape in corel.obtener_shapes():
    analizador.analizar(shape)

resumen = ResumenProduccion(
    analizador.obtener_resumen(),
    analizador.obtener_no_reconocidos()
)

resumen.mostrar()