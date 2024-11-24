import flet as ft

class Cart:
    def create_card(self, level):
        """Crea una tarjeta para mostrar un nivel."""
        # Validación: asegurarse de que level es un diccionario con las claves requeridas
        required_keys = ['name', 'description', 'complete']
        for key in required_keys:
            if key not in level:
                raise ValueError(f"El diccionario level debe contener la clave '{key}'. Claves actuales: {list(level.keys())}")
        
        # Construir componentes de la tarjeta
        title = ft.Text(value=level['name'])
        description = ft.Text(value=level['description'])
        complete_text = "Incompleto" if not level['complete'] else "Completo"
        complete = ft.Text(value=complete_text)  # Convertir a texto si es necesario
        
        # Retornar la tarjeta construida
        return ft.Card(
            width=155,
            height=150,
            content=ft.Container(
                col=6,
                content=ft.Column(
                    controls=[
                        title,
                        description,
                        ft.Row(
                            controls=[complete],
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
