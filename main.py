import flet as ft
from models.levls_models import levels_models # Importar el modelo para obtener datos

def create_card(level):
    """Crea una tarjeta para mostrar un nivel."""
    title = ft.Text(value=level['name'],)
    description = ft.Text(level['description'])
    complete=ft.Text(level['complete'])
    return ft.Card(
        width=180,
        content=ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    description,
                    ft.Row(
                        controls=[
                            complete
                        ],
                        alignment='end'
                    )
                ],
                spacing=10,
            ),
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.SURFACE_VARIANT,
        ),
        elevation=3,
    )

def levels_view(page: ft.Page):
    """Crea la vista que muestra tarjetas dinámicamente según levels_models."""
    page.title = "Lista de Niveles"
    page.scroll = "adaptive"

    # Instanciar el modelo y obtener los niveles
    model =levels_models()
    niveles = model.get_levels()

    # Verificar si hay datos
    if not niveles:
        page.add(ft.Text("No se encontraron niveles o hubo un error al obtenerlos.", color="red"))
        return

    # Crear tarjetas dinámicamente para cada nivel
    cards = [create_card(nivel) for nivel in niveles]

    # Añadir las tarjetas a la página
    page.add(
        ft.Column(
            controls=cards,
            spacing=20,
        )
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=levels_view)
