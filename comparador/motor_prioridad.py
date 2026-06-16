from comparador.configuracion_prioridad import PRIORIDAD_PRENDAS, DEPENDENCIAS
from comparador.configuracion_prendas import PRENDAS


class MotorPrioridad:

    def asignar(self, resumen):

        disponible = resumen.copy()
        produccion = {}

        for prenda in PRIORIDAD_PRENDAS:

            piezas_necesarias = PRENDAS.get(prenda)
            if not piezas_necesarias:
                continue

            tallas = self._extraer_tallas(disponible)

            for talla in tallas:

                # 🔥 SI ES COMPUESTA, VALIDAR COMPLETA PRIMERO
                if prenda in DEPENDENCIAS:

                    posibles = self._calcular_compuesta(prenda, talla, disponible)

                else:

                    posibles = self._calcular_simple(piezas_necesarias, talla, disponible)

                if posibles <= 0:
                    continue

                produccion[f"{prenda} {talla}"] = posibles

                # consumir piezas
                for pieza in piezas_necesarias:
                    clave = f"{pieza} {talla}"
                    disponible[clave] -= posibles

        return produccion


    def _extraer_tallas(self, resumen):

        tallas = set()

        for clave in resumen.keys():

            partes = clave.rsplit(" ", 1)

            if len(partes) == 2:
                tallas.add(partes[1])

        return sorted(list(tallas))
    

    def _validar_dependencias(self, prenda, talla, disponible):

        for dep in DEPENDENCIAS[prenda]:

            clave = f"{dep} {talla}"

            if disponible.get(clave, 0) <= 0:
                return False

        return True
    

    def _calcular_compuesta(self, prenda, talla, disponible):

        cantidades = []

        for dep in DEPENDENCIAS[prenda]:

            clave = f"{dep} {talla}"
            cantidades.append(disponible.get(clave, 0))

        return min(cantidades)
    

    def _calcular_simple(self, piezas, talla, disponible):

        cantidades = []

        for pieza in piezas:

            clave = f"{pieza} {talla}"
            cantidades.append(disponible.get(clave, 0))

        return min(cantidades)