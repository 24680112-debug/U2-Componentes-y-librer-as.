# U2 Componentes y librerías.

## Apuntes de clase

## Introducción
En esta unidad, aprenderemos a organizar nuestro código de manera eficiente, reutilizando funcionalidades y creando nuestros propios componentes, tanto visuales como no visuales. Usaremos la librería Flet (para interfaces de usuario) y Matplotlib (para gráficas) como herramientas principales.

## 2.1 Definición conceptual de componentes, paquetes / librerías
Conceptos Clave
* Componente: Es una unidad de software reutilizable y autónoma. En programación orientada a objetos, una clase suele actuar como un plano para un componente. En Flet, casi todo es un componente (un botón, un contenedor, una columna).

* Librería (Biblioteca): Es una colección de código preescrito que los desarrolladores pueden utilizar para realizar tareas comunes sin tener que programarlo todo desde cero. Una librería suele resolver un problema específico.

* Paquete: Es una forma de organizar módulos (archivos de código) relacionados en un directorio. En Python, un directorio que contiene un archivo **`__init__.py`** se considera un paquete.

Ejemplo Relacionado (Código: **`grafica.py`**)
En el archivo **`grafica.py`**, vemos la aplicación práctica de estos conceptos al principio del código:  
```bash
import matplotlib.pyplot as plt
import flet as ft
import flet_charts as fch
import random
```

Análisis:

* Estamos importando librerías.

* **`matplotlib.pyplot`** es una librería para crear gráficas.

* **`flet`** es una librería para crear interfaces de usuario.

* **`flet_charts`** es otra librería (o paquete) especializada en integrar gráficas en Flet.

* **`random`** es una librería estándar de Python para generar datos aleatorios.

* Cada una de estas librerías nos proporciona "componentes" y funciones listos para usar (por ejemplo, **`plt.subplots()`**, **`ft.Page`**, **`ft.Container`**, **`random.randint()`**).

## 2.2 Uso de librerías proporcionadas por el lenguaje
Conceptos Clave
Python viene con una amplia "Biblioteca Estándar" que proporciona herramientas para interactuar con el sistema operativo, trabajar con archivos, generar números aleatorios, etc. No necesitamos instalar nada adicional para usarlas.

Ejemplo Relacionado (Código: **`tijeras.py`** - Piedra, Papel o Tijera)
En el juego de Piedra, Papel o Tijera (**`tijeras.py`**), utilizamos la librería estándar **`random`** para simular la elección de la computadora.

Código de ejemplo en **`tijeras.py`**:
```bash
import random  # <-- Importamos la librería estándar

# ... dentro de la función main y la función jugar ...
opciones = ["Piedra", "Papel", "Tijeras"]

def jugar(e):
    # ...
    sistema = random.choice(opciones)  # <-- Usamos una función de la librería
    # ...
```

Análisis:

1. **`import random`**: Importamos la librería proporcionada por Python.

2. **`random.choice(opciones)`**: Utilizamos la función **`choice`** de esa librería para seleccionar aleatoriamente un elemento de la lista **`opciones`**. Este es un uso directo y sencillo de una librería estándar.

## 2.3 Creación de componentes (visuales y no visuales) definidos por el usuario
Esta es una de las partes más importantes para crear aplicaciones escalables y mantenibles. En lugar de copiar y pegar código, creamos nuestras propias "piezas" reutilizables.

Componente Visual Definido por el Usuario
Es un componente que tiene una representación gráfica en la interfaz. Lo creamos creando una clase que hereda de un componente base de Flet (como **`ft.Container`**).

Ejemplo Relacionado (Código: **`componente.py}**)
En este archivo, creamos una tarjeta de perfil de usuario reutilizable.

Código de ejemplo en **`componente.py`**:
```bash
import flet as ft

# Definición del componente personalizado VISUAL (Hereda de ft.Container)
class TarjetaPerfil(ft.Container):
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        # 1. Llamada al constructor de la clase padre (ft.Container)
        super().__init__()

        # 2. Definimos el contenido visual internamente
        self.content = ft.Column(
            controls=[
                ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )

        # 3. Configuramos propiedades visuales del contenedor base
        self.border = ft.border.all(2, color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    # Lógica asociada al componente (Método)
    def saludar(self, e):
        print(f"Interactuando con el componente de {self.content.controls[0].value}")
```

Uso del Componente Visual:
```bash
def main (page: ft.Page):
    # ...
    # Instanciamos (creamos) nuestros componentes personalizados
    # Son reutilizables, solo cambiamos los datos
    usuario1 = TarjetaPerfil("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software") # Usa color por defecto

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        # Agregamos los componentes a la página
        ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
    )
```

Análisis:

* **`class TarjetaPerfil(ft.Container)`**: Indica que estamos creando un nuevo componente que es un **`ft.Container`**, pero con más funcionalidades definidas por nosotros.

* El constructor **`__init__`** se encarga de estructurar cómo se verá y comportará esa tarjeta cada vez que creemos una nueva.

* **`self.content`**: Definimos el diseño interno (Texto, Botón) una sola vez.

* En **`main`**, creamos dos instancias diferentes (**`usuario1`**, **`usuario2`**) usando la misma "plantilla" (**`TarjetaPerfil`**), lo que demuestra la reutilización.

Componente No Visual Definido por el Usuario
Es un componente que maneja datos o lógica, pero no se "dibuja" directamente en la pantalla. Sirve para encapsular información de manera estructurada.

Ejemplo Relacionado (Código: **`clases.py`** y **`dataclass.py`**)
En estos ejemplos, definimos una clase para representar los datos de un **`Usuario`**.

Opción A: Clase Normal (**`clases.py`**)
```bash
# Componente NO VISUAL (Solo datos)
class Usuario:
    def __init__(self, nombre, rol, color=ft.Colors.BLUE):
        self.nombre = nombre
        self.rol = rol
        self.color = color
```

Opción B: Dataclass (**`dataclass.py`**)
```bash
from dataclasses import dataclass

# Componente NO VISUAL usando dataclass (forma más moderna y concisa)
@dataclass
class Usuario:
    nombre: str
    rol: str
    color: ft.Colors = ft.Colors.BLUE # Valor por defecto
```

Integración: Componente No Visual -> Componente Visual

Ahora, nuestro componente visual **`TarjetaPerfil`** puede aceptar una instancia de este componente no visual (**`Usuario`**) como parámetro, separando mejor los datos de la vista.
```bash
# En componente_clases_normal.py / componente_dataclass.py
class TarjetaPerfil(ft.Container):
    # Ahora recibe un objeto 'usuario' en lugar de parámetros sueltos
    def __init__(self, usuario: Usuario):
        super().__init__()
        self.usuario = usuario # Guardamos la referencia a los datos

        self.content = ft.Column(
            controls=[
                # Usamos los datos del objeto 'usuario'
                ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(usuario.rol, italic=True),
                # ...
            ],
            # ...
        )
        # Usamos el color definido en el objeto de datos
        self.border = ft.border.all(2, usuario.color)
        # ...

# En el main
def main(page: ft.Page):
    # 1. Creamos componentes NO VISUALES (Datos)
    u1 = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    u2 = Usuario("Carlos Ruiz", "Arquitecto de Software")

    # 2. Creamos componentes VISUALES pasándoles los datos
    tarjeta1 = TarjetaPerfil(u1)
    tarjeta2 = TarjetaPerfil(u2)

    # 3. Mostramos las tarjetas
    page.add(ft.Row([tarjeta1, tarjeta2]))
```

Análisis:

* Esta aproximación es superior porque separa las responsabilidades. La clase **`Usuario`** solo sabe sobre datos (nombre, rol). La clase **`TarjetaPerfil`** solo sabe cómo mostrar esos datos.

* Usar **`@dataclass`** es preferible para clases que solo contienen datos, ya que Python genera automáticamente el constructor y otros métodos útiles, haciendo el código más limpio.

## 2.4 Creación y uso de paquetes/librerías definidas por el usuario
Conceptos Clave
Cuando nuestro proyecto crece y tenemos muchos componentes personalizados (**`TarjetaPerfil`**, **`BotonEspecial`**, **`MenuNavegacion`**, etc.), no queremos tener todo en un solo archivo gigante. Lo ideal es agruparlos en un paquete.

Para crear tu propio paquete:

1. Crea una carpeta (ej. **`mis_componentes`**).

2. Mueve tus archivos de componentes a esa carpeta (ej. **`tarjeta.py`**, **`boton.py`**).

3. Crea un archivo vacío llamado **`__init__.py`** dentro de la carpeta **`mis_componentes`**.

Ahora puedes importar tus componentes en tu archivo principal:
```bash
# Archivo: main.py
import flet as ft
# Importamos desde NUESTRO propio paquete
from mis_componentes.tarjeta import TarjetaPerfil
from mis_componentes.boton import BotonEspecial

def main(page: ft.Page):
    # ... uso de los componentes importados ...
    pass

ft.app(target=main)
```

Ejemplo en el Código Proporcionado
Aunque no tenemos la estructura de carpetas visible en los snippets, el código de los archivos **`dataclass.py`** y **`clases.py`** está estructurado para que, si moviéramos las definiciones de las clases **`Usuario`** y **`TarjetaPerfil`** a un archivo separado (ej. ui_models.py), podríamos importarlos fácilmente en otros scripts de la misma manera:

**`from ui_models import Usuario, TarjetaPerfil`**

Esto facilitaría la reutilización de estos componentes en múltiples aplicaciones dentro de un proyecto más grande.

Resumen de Relaciones Tema-Código:

| Subtema | Código de Ejemplo Destacado | Concepto Clave Aplicado |
| :--- | :---: | ---: |
| 2.1 Definición conceptual... | **`grafica.py`** | Uso de **`import`** para traer librerías (**`flet`**, **`matplotlib`**). |
| 2.2 Uso de librerías proporcionadas... | **`tijeras.py`** | Uso de **`import random`** (librería estándar) para la lógica del juego. |
| 2.3 Creación de componentes...| **`componentes.py`** | Creación de **`class TarjetaPerfil(ft.Container)`** como componente visual reusable. |
| 2.3 Creación de componentes...| **`dataclass.py`** | Creación de **`@dataclass Usuario`** como componente no visual (datos). |
| 2.4 Creación y uso de paquetes... | (Concepto) **`dataclass.py`** | El código está preparado para ser modularizado e importado desde un paquete propio. |


## Referencias bibliográficas
* Sommerville, I. (2011). Ingeniería de software (9.ª ed.). Pearson Educación.
* Python Software Foundation. (2026). Modules and Packages. Python 3.12 Documentation. https://docs.python.org/3/tutorial/modules.html
* Pressman, R. S., & Maxim, B. R. (2021). Ingeniería de software: Un enfoque práctico (9.ª ed.). McGraw-Hill.
