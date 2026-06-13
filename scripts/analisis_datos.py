"""
analisis_datos.py - Escenario B: Analisis de Ventas de una Pequena Empresa.
TP Gestion Colaborativa - Organizacion Empresarial (UTN-TUP).

Que hace:
  1. Lee el dataset de ventas (datos/ventas.csv).
  2. Calcula indicadores: ventas totales, producto mas vendido y ventas por mes.
  3. Genera un grafico con la evolucion mensual de las ventas.
  4. Guarda los resultados en la carpeta resultados/.

No usa rutas absolutas: resuelve las rutas a partir de la ubicacion del propio
archivo, por lo que funciona igual en una PC local o en Google Colab.
"""

from pathlib import Path

import pandas as pd
import matplotlib
# Backend 'Agg' (sin ventana grafica) PORQUE Colab no tiene pantalla:
# asi el grafico se genera y se guarda como imagen sin abrir ventanas.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# BASE_DIR es la raiz del repo (carpeta que contiene scripts/, datos/, resultados/).
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_DATOS = BASE_DIR / "datos" / "ventas.csv"
DIR_RESULTADOS = BASE_DIR / "resultados"
DIR_RESULTADOS.mkdir(exist_ok=True)


def cargar_datos(ruta):
    """Carga el CSV y agrega la columna de importe (cantidad x precio)."""
    df = pd.read_csv(ruta, parse_dates=["fecha"])
    df["importe"] = df["cantidad"] * df["precio"]
    return df


def calcular_indicadores(df):
    """Calcula los indicadores de negocio solicitados en el escenario."""
    ventas_totales = df["importe"].sum()
    # "Mas vendido" se mide de dos formas: por unidades y por dinero facturado.
    unidades_por_producto = df.groupby("producto")["cantidad"].sum()
    importe_por_producto = df.groupby("producto")["importe"].sum()
    ventas_por_mes = df.groupby(df["fecha"].dt.to_period("M"))["importe"].sum().sort_index()
    return {
        "ventas_totales": ventas_totales,
        "cantidad_operaciones": len(df),
        "producto_top_unidades": unidades_por_producto.idxmax(),
        "producto_top_importe": importe_por_producto.idxmax(),
        "unidades_por_producto": unidades_por_producto.sort_values(ascending=False),
        "ventas_por_mes": ventas_por_mes,
    }


def graficar_ventas_mensuales(ventas_por_mes, destino):
    """Genera y guarda el grafico de evolucion mensual de las ventas."""
    etiquetas = ventas_por_mes.index.astype(str)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(etiquetas, ventas_por_mes.values, marker="o", linewidth=2)
    ax.set_title("Evolucion de las ventas mensuales - 2025")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Facturacion (ARS)")
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig(destino, dpi=150)
    plt.close(fig)


def guardar_resumen(indicadores, destino):
    """Exporta una tabla resumen de los indicadores a un CSV."""
    resumen = pd.DataFrame({
        "indicador": [
            "Ventas totales (ARS)",
            "Cantidad de operaciones",
            "Producto mas vendido (unidades)",
            "Producto que mas factura (ARS)",
        ],
        "valor": [
            round(indicadores["ventas_totales"], 2),
            indicadores["cantidad_operaciones"],
            indicadores["producto_top_unidades"],
            indicadores["producto_top_importe"],
        ],
    })
    resumen.to_csv(destino, index=False, encoding="utf-8")


def main():
    df = cargar_datos(RUTA_DATOS)
    indicadores = calcular_indicadores(df)

    print("=== Analisis de ventas - Escenario B ===")
    print(f"Operaciones analizadas : {indicadores['cantidad_operaciones']}")
    print(f"Ventas totales         : $ {indicadores['ventas_totales']:,.0f}")
    print(f"Top por unidades       : {indicadores['producto_top_unidades']}")
    print(f"Top por facturacion    : {indicadores['producto_top_importe']}")
    print("\nVentas por mes:")
    print(indicadores["ventas_por_mes"].to_string())

    graficar_ventas_mensuales(indicadores["ventas_por_mes"], DIR_RESULTADOS / "ventas_por_mes.png")
    guardar_resumen(indicadores, DIR_RESULTADOS / "resumen_indicadores.csv")
    print("\nResultados guardados en la carpeta resultados/")


if __name__ == "__main__":
    main()
