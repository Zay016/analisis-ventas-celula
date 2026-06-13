# Análisis de Ventas de una Pequeña Empresa

Trabajo Práctico de **Gestión Colaborativa, Control de Versiones y Organización
Empresarial** (Git, GitHub y Jira).
Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional.
Cátedra: **Organización Empresarial** — Año lectivo 2026.

## Integrantes del equipo

| Rol | Responsable | Usuario de GitHub |
|-----|-------------|-------------------|
| P1 — Líder y Organizador (Hugo) | Zaylene Gascon | @Zay016 |
| P2 — Desarrollador Técnico (Paco) | Zaylene Gascon | @Zay016 |
| P3 — Revisor y QA (Luis) | Zaylene Gascon | @Zay016 |

## Escenario elegido

**Escenario B — Análisis de Ventas de una Pequeña Empresa.**
El proyecto procesa un conjunto de datos de ventas comerciales para generar
indicadores básicos que permiten interpretar el desempeño del negocio.

## Descripción del dataset

Archivo: `datos/ventas.csv` (180 operaciones de venta del año 2025).

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `producto` | texto | Nombre del producto vendido |
| `cantidad` | entero | Unidades vendidas en la operación |
| `precio` | entero | Precio unitario en pesos argentinos (ARS) |
| `fecha` | fecha | Fecha de la venta (formato AAAA-MM-DD) |

El dataset fue generado de forma reproducible (semilla fija) y representa ventas
simuladas de una pequeña empresa de tecnología.

## Indicadores que calcula el análisis

- Ventas totales (facturación = cantidad × precio).
- Producto más vendido por unidades y por facturación.
- Ventas agrupadas por mes.
- Gráfico de la evolución mensual de las ventas.

## Estructura del repositorio
