import matplotlib.pyplot as plt
import flet as ft
import flet_charts as fch
import random  # Para simular datos de sensores

# --- FUNCIONES DE GRÁFICAS ---

def generar_grafica_barras():
    productos = ["Celulares", "Laptops", "Audífonos", "Smartwatch"]
    ventas = [15, 30, 45, 10]
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(productos, ventas, color="skyblue")
    ax.set_title("Ventas por Producto", fontsize=10, weight='bold')
    plt.tight_layout()
    return fig


def generar_grafica_lineas():
    meses = ["Ene", "Feb", "Mar", "Abr", "May"]
    rendimiento = [10, 25, 18, 40, 35]
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(meses, rendimiento, color="orange", marker='o', linewidth=2)
    ax.set_title("Tendencia de Rendimiento", fontsize=10, weight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig


def generar_grafica_dispersion():
    x = [i for i in range(20)]
    y = [random.randint(10, 50) for _ in range(20)]

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.scatter(x, y, color="purple", alpha=0.6, edgecolors="white")
    ax.set_title("Muestreo de Sensores", fontsize=10, weight='bold')

    plt.tight_layout()
    return fig


# --- NUEVA FUNCIÓN: GRÁFICA DE PASTEL ---

def generar_grafica_pastel():
    categorias = ["Tecnología", "Salud", "Educación", "Otros"]
    valores = [35, 25, 20, 20]
    colores = ["#4CAF50", "#FF9800", "#2196F3", "#9C27B0"]

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.pie(
        valores,
        labels=categorias,
        autopct="%1.1f%%",
        startangle=90,
        colors=colores
    )
    ax.set_title("Distribución de Categorías", fontsize=10, weight='bold')
    ax.axis("equal")

    plt.tight_layout()
    return fig


def main(page: ft.Page):
    page.title = "Dashboard TAP - Gráfica 4"
    page.theme_mode = "light"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    header = ft.Text(
        "Dashboard de Visualización de Gráficas",
        size=24,
        weight="bold"
    )

    tablero = ft.GridView(
        expand=True,
        runs_count=2,
        spacing=20,
        run_spacing=20,
        child_aspect_ratio=1.5,
    )

    # --- GRÁFICA 1: BARRAS ---
    fig_1 = generar_grafica_barras()
    contenedor_1 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_1),
        border=ft.border.all(1, "black12"),
        border_radius=10,
        padding=5
    )
    plt.close(fig_1)

    # --- GRÁFICA 2: LÍNEAS ---
    fig_2 = generar_grafica_lineas()
    contenedor_2 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_2),
        border=ft.border.all(1, "black12"),
        border_radius=10,
        padding=5
    )
    plt.close(fig_2)

    # --- GRÁFICA 3: DISPERSIÓN ---
    fig_3 = generar_grafica_dispersion()
    contenedor_3 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_3),
        border=ft.border.all(1, "black12"),
        border_radius=10,
        padding=5
    )
    plt.close(fig_3)

    # --- GRÁFICA 4: PASTEL ---
    fig_4 = generar_grafica_pastel()
    contenedor_4 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_4),
        border=ft.border.all(1, "black12"),
        border_radius=10,
        padding=5
    )
    plt.close(fig_4)

    # Cargamos los controles al tablero
    tablero.controls.append(contenedor_1)
    tablero.controls.append(contenedor_2)
    tablero.controls.append(contenedor_3)
    tablero.controls.append(contenedor_4)

    page.add(header, ft.Divider(), tablero)


if __name__ == "__main__":
    ft.app(target=main)