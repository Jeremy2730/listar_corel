
# Listar Corel

## Objetivo

Analizar automáticamente documentos de CorelDRAW para identificar piezas textiles mediante sus medidas, clasificarlas por producto y talla, consolidar múltiples documentos de producción y comparar el resultado contra un pedido solicitado.

---

# Funcionalidades implementadas

## Integración con CorelDRAW

* Conexión automática a CorelDRAW.
* Detección de documento abierto.
* Protección cuando CorelDRAW no está disponible.
* Lectura automática de páginas.
* Lectura automática de shapes.
* Análisis directo sobre el documento activo.

---

## Catálogos de producción

Actualmente soporta:

* Camisetas
* Mangas
* Mangas largas
* Pantalonetas

Cada catálogo contiene las medidas oficiales por talla.

---

## Identificación automática

* Reconocimiento por medidas.
* Tolerancia configurable para pequeñas diferencias.
* Clasificación automática por:
  * Producto
  * Talla

Ejemplos:

```text
camiseta XL
camiseta M
manga M
pantaloneta 12
```

---

## Gestión de listados

El sistema permite crear un listado de producción persistente.

Cada listado almacena:

* Nombre del listado.
* Fecha de creación.
* Documentos agregados.
* Acumulado general de piezas.

Funciones disponibles:

* Crear listado.
* Agregar documento.
* Eliminar documento.
* Eliminar listado.
* Consultar listado activo.

---

## Acumulado de producción

Al agregar documentos:

* Se evita duplicar documentos.
* Se consolidan automáticamente las piezas.
* Se recalcula el acumulado general.

Ejemplo:

```text
camiseta XL -> 2
manga XL -> 2
pantaloneta XL -> 2
```

---

## Conversión de piezas a prendas

El sistema convierte automáticamente las piezas detectadas en prendas reales.

### Camisetas

Una camiseta completa equivale a:

```text
2 piezas camiseta
+
2 mangas
=
1 camiseta
```

### Pantalonetas

Una pantaloneta completa equivale a:

```text
2 piezas pantaloneta
=
1 pantaloneta
```

Ejemplo:

```text
camiseta XL -> 2 piezas
manga XL -> 2 piezas
```

Se convierte automáticamente en:

```text
camiseta XL -> 1 prenda
```

---

## Comparador de pedidos

Implementado:

### Pedido manual

Permite ingresar cantidades por talla para:

* Camisetas
* Pantalonetas

Posteriormente compara:

```text
Pedido
vs
Producción real
```

Mostrando:

* COMPLETO
* FALTAN
* SOBRAN

Ejemplo:

```text
camiseta M      Pedido: 4   Prod: 4   COMPLETO
camiseta XL     Pedido: 2   Prod: 1   FALTAN 1
```

También calcula:

```text
Faltantes totales
Sobrantes totales
```

---

## Orden de tallas

Todo el sistema utiliza un orden único:

```text
5XL
4XL
3XL
2XL
XL
L
M
S
16
14
12
10
8
6
4
2
0
```

---

## Manejo de errores

* CorelDRAW cerrado.
* Documento no abierto.
* Documento duplicado.
* Listado inexistente.
* Acumulados vacíos.
* Piezas no reconocidas.

---

# Persistencia

## PedidoManager

Responsable de:

* Guardar listado.
* Cargar listado.
* Eliminar listado.

Archivo:

```text
datos/pedido_base.json
```

---

## EstadoManager

Responsable de:

* Guardar estado de la aplicación.
* Detectar listado activo.

Archivo:

```text
datos/estado.json
```

Ejemplo:

```json
{
    "pedido_activo": true
}
```

---

# Estructura actual

```text
listar_corel/
├── analizadores/
├── catalogos/
├── comparador/
├── configuracion/
├── corel/
├── datos/
├── modelos/
├── pedidos/
├── tests/
├── ui/
├── main.py
├── README.md
└── requirements.txt
```

---

# Arquitectura principal

```text
Menu
│
└── OperacionesListado
    ├── crear_listado()
    ├── agregar_documento()
    ├── eliminar_documento()
    ├── ver_acumulado()
    ├── comparar_pedido()
    └── eliminar_listado()
```

---

# Estado actual

Proyecto estable.

Funcionalidades completadas:

* Persistencia de listados.
* Acumulado de múltiples documentos.
* Conversión de piezas a prendas.
* Comparador manual de pedidos.
* Administración de documentos.
* Ordenamiento unificado por tallas.
* Refactorización del módulo de comparación.

---

# Próximas fases

## Fase 1

Comparación mediante Excel.

```text
Comparar pedido
├── Manual
└── Excel
```

---

## Fase 2

Plantilla estándar de importación.

---

## Fase 3

Reportes de producción.

* Faltantes.
* Sobrantes.
* Cumplimiento por talla.

---

## Fase 4

Diferenciación completa de piezas.

Ejemplo:

```text
delantero
espalda
manga izquierda
manga derecha
```

para aumentar la precisión del análisis.

---

## Fase 5

Automatización avanzada para producción textil basada en CorelDRAW.
