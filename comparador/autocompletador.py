class Autocompletador:

    MAPA_PRENDAS = {

        "cami": "camiseta",
        "camiseta": "camiseta",
        "camisetas": "camiseta",
        "cm": "camiseta",

        "buso": "buso",
        "busos": "buso",
        "buzo": "buso",
        "buzos": "buso",
        "bs": "buso",

        "pantaloneta": "pantaloneta",
        "pan": "pantaloneta",
        "pantalonetas": "pantaloneta",
        "pl": "pantaloneta",

        "peto": "peto",
        "petos": "peto",
        "pe": "peto",

        "uni": "uniforme",
        "uniforme": "uniforme", 
        "uniformes": "uniforme", 

        "ub": "uniforme_buso",
        "up": "uniforme_peto"
    }

    def completar(self, prenda):

        prenda = prenda.lower().strip()

        return self.MAPA_PRENDAS.get(prenda, prenda)