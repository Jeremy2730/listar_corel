# Listar Corel

## Objetivo

Analizar automáticamente documentos de CorelDRAW para identificar piezas textiles, clasificarlas por talla y producto, y posteriormente comparar pedidos de producción.

---

## Funcionalidades implementadas

### Corel

- Conexión automática a CorelDRAW.
- Detección de documento abierto.
- Protección cuando Corel no está abierto.
- Lectura de páginas y capas.
- Lectura de shapes.

### Catálogos

- Camisetas.
- Mangas.
- Mangas largas.
- Pantalonetas.

### Identificación

- Detección automática por medidas.
- Tolerancia para diferencias de tamaño.
- Clasificación por:
  - Producto.
  - Talla.

### Producción

- Resumen agrupado por talla.
- Orden de impresión:
  - 5XL
  - 4XL
  - 3XL
  - 2XL
  - XL
  - L
  - M
  - S
  - 16
  - 14
  - 12
  - 10
  - 8
  - 6
  - 4

### Control de errores

- No falla si Corel está cerrado.
- No falla si no hay documento abierto.
- Reporta piezas no reconocidas.

---

## Persistencia

### PedidoManager

Permite:

- Guardar pedido base.
- Cargar pedido base.
- Eliminar pedido base.

Archivo:

```text
datos/pedido_base.json
```

### EstadoManager

Permite:

- Guardar estado.
- Leer estado.

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

## Estructura actual

```text
listar_corel/
├── analizadores/
├── catalogos/
├── corel/
├── datos/
│   ├── estado.json
│   └── pedido_base.json
├── pedidos/
│   ├── pedido_manager.py
│   ├── estado_manager.py
│   └── resumen_produccion.py
├── tests/
├── ui/
├── main.py
└── modelos.py
```

---

## Próximas fases

### Fase 1

Crear:

```text
ui/menu.py
```

Objetivo:

- Crear pedido base.
- Continuar pedido.
- Eliminar pedido.
- Solo listar documento.

### Fase 2

Detección automática de pedido activo.

Al iniciar:

```text
Hay un pedido guardado.

1. Continuar pedido
2. Crear nuevo pedido
3. Eliminar pedido
4. Solo listar documento actual
```

### Fase 3

Guardar pedido base desde documento abierto.

### Fase 4

Comparación de documentos de producción contra pedido base.

### Fase 5

Control de avance:

- Archivos revisados.
- Piezas encontradas.
- Faltantes.
- Sobrantes.

---

## Estado actual

Proyecto estable.

Última funcionalidad completada:

- Resumen de producción por talla.
- Persistencia mediante PedidoManager y EstadoManager.
