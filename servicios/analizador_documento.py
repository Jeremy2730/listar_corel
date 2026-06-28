from analizadores.analizador_piezas import AnalizadorPiezas

def analizar_documento(corel):

    analizador = AnalizadorPiezas()

    for shape in corel.obtener_shapes():

        analizador.analizar(shape)

    return analizador