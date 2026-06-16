# Configuración de prioridad para prendas y dependencias 

PRIORIDAD_PRENDAS = [
    "camiseta",
    "buso",
    "peto",
    "pantaloneta",

    "uniforme",
    "uniforme_buso",
    "uniforme_peto"
]

DEPENDENCIAS = {
    "uniforme": ["camiseta", "pantaloneta"],
    "uniforme_buso": ["buso", "pantaloneta"],
    "uniforme_peto": ["peto", "pantaloneta"]
}