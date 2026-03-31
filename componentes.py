import flet as ft

# Definición del componente personalizado (Subtema 2.3)
class TarjetaPerfil(ft.Container):
    def _init_(self, nombre, rol, color_borde=ft.Colors.BLUE):
        super()._init_()
        self.content = ft.Column(
            controls=[
                ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20), 
                ft.Text(rol, italic=True), 
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )
        self.border = ft.border.all(2, color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        print(f" Interactuando con el componente de {self.content.controls[0].value}")

def main (page: ft.Page):
    page.title = "Unidad 2: Componentes Definidos por el Usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Instanciando nuestros componentes personalizados
    usuario1 = TarjetaPerfil("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"), 
        ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)