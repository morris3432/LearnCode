import flet as ft 

def main(page: ft.Page):
    page.window.height = 800
    page.window.width = 380
    page.window.resizable = False
    page.theme = ft.Theme(color_scheme_seed="blue")
    
    # funciones
    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    # componentes    
    
    dialogWelcome = ft.AlertDialog(
        modal=True
        ,title=ft.Text('Bienvenido')
        ,content=ft.Text('Benvenido a Learn Code donde aprenderas a programar')
        ,actions=[
            ft.TextButton("Continuar", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END
        ,on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        )
    )
    
    
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    btn2 = ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal))
    btn = ft.ElevatedButton("Close modal dialog", on_click=lambda e: page.open(dialogWelcome))
    
    container = ft.Container(
        width=350,
        height=745,
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLACK,
        content=ft.Column(
            controls=[
                btn2
                ,ft.Divider(height=5, color=ft.colors.TRANSPARENT)
                ,btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    # agregar componentes a la página
    page.add(container)



# función principal
ft.app(target=main)