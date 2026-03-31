import flet as ft
from dataclasses import dataclass

# Clase de datos con dataclass
@dataclass
class Usuario:
    nombre: str
    rol: str
    color: ft.Colors = ft.Colors.BLUE


# Componente visual personalizado
class TarjetaPerfil(ft.Container):

    def __init__(self, usuario: Usuario):
        super().__init__()

        self.usuario = usuario

        self.content = ft.Column(
            controls=[
                ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(usuario.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )

        self.border = ft.border.all(2, usuario.color)
        self.padding = 10
        self.border_radius = 10
        self.width = 220


    def saludar(self, e):
        print(f"Interactuando con el componente de {self.usuario.nombre}")


def main(page: ft.Page):

    page.title = "Ejemplo usando dataclass"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario1 = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = Usuario("Carlos Ruiz", "Arquitecto de Software")

    tarjeta1 = TarjetaPerfil(usuario1)
    tarjeta2 = TarjetaPerfil(usuario2)

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight=ft.FontWeight.BOLD),
        ft.Row([tarjeta1, tarjeta2], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)