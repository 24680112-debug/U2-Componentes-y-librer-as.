import flet as ft
import random

def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijeras"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    opciones = ["Piedra", "Papel", "Tijeras"]

    resultado_texto = ft.Text(size=20, weight="bold")
    eleccion_usuario = ft.Text()
    eleccion_sistema = ft.Text()

    def jugar(e):
        usuario = e.control.content.value
        sistema = random.choice(opciones)

        eleccion_usuario.value = f"Tú elegiste: {usuario}"
        eleccion_sistema.value = f"El sistema eligió: {sistema}"

        if usuario == sistema:
            resultado_texto.value = "¡Es un empate!"
        elif (
            (usuario == "Piedra" and sistema == "Tijeras") or
            (usuario == "Papel" and sistema == "Piedra") or
            (usuario == "Tijeras" and sistema == "Papel")
        ):
            resultado_texto.value = "¡Ganaste! "
        else:
            resultado_texto.value = "¡Perdiste! "

        page.update()

    page.add(
        ft.Text("Elige una opción:", size=25, weight="bold"),
        ft.Row(
            [
                ft.ElevatedButton(content=ft.Text("Piedra"), on_click=jugar),
                ft.ElevatedButton(content=ft.Text("Papel"), on_click=jugar),
                ft.ElevatedButton(content=ft.Text("Tijeras"), on_click=jugar),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        eleccion_usuario,
        eleccion_sistema,
        resultado_texto
    )

ft.app(target=main)