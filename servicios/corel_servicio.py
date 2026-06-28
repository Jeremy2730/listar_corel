# servicios/corel_servicio.py

from corel.corel_api import CorelAPI

def obtener_corel():

    corel = CorelAPI()

    if not corel.conectar():
        return None

    return corel