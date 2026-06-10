from corel.corel_api import CorelAPI
from analizadores.analizador_piezas import AnalizadorPiezas

corel = CorelAPI()

if corel.conectar():

    analizador = AnalizadorPiezas()

    for shape in corel.obtener_shapes():

        analizador.analizar(shape)

    analizador.mostrar_resumen()