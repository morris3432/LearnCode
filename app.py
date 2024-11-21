import flet as ft 

def main(page: ft.Page):
    page.window.height = 800
    page.window.width = 380
    page.window.resizable = False
    page.theme = ft.Theme(color_scheme_seed="blue")
    
    # funciones
    def handle_close(e):
        page.close(dialogWelcome)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def advertisement(e):
        page.close(advert)
        
    advert = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error", size=20, weight=ft.FontWeight.W_900),
            content=ft.Text("Por favor, ingrese su correo y contraseña, para poder iniciar sesión"),
            actions=[
                ft.TextButton("Aceptar", on_click=advertisement),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(
                ft.Text("Modal dialog dismissed"),
            ),
    )
    # componentes        
    dialogWelcome =ft.AlertDialog(
        modal=True,
        title=ft.Text("Learn Code" , size=20, weight=ft.FontWeight.W_900),
        content=ft.Text("Bienvenido a Learn Code donde aprenderas a programar"),
        actions=[
            ft.TextButton("Aceptar", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )
    
    levels=ft.Container(visible=True,expand=True,bgcolor=ft.colors.PURPLE_900)

    btn2 = ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dialogWelcome))

    email=ft.TextField(
        hint_text='E-Mail'
        ,border='underline'
        ,color='blue'
        ,prefix_icon=ft.icons.EMAIL
    )
    
    password=ft.TextField(
        hint_text='Contraseña'
        ,border='underline'
        ,color='blue'
        ,prefix_icon=ft.icons.LOCK
        ,password=True
        ,can_reveal_password= True
    )

    conf=ft.Container(
        expand=True,
        bgcolor='violet',
        visible=True,
        content=ft.Text(str(email.value))
    )        

    
    def login_registrer(e):
        if e == 0:
            print('login_registrer')
        
    container = ft.Container(
        visible=False,
        width=350,
        height=745,
        padding=5,
        border_radius=10,
        bgcolor=ft.colors.BLACK,
        content=ft.Column(
            controls=[
                ft.Stack(
                    expand=True
                    ,controls=[
                        conf
                    ]
                )
                ,ft.Container(border_radius=8 ,height=50,bgcolor=ft.colors.BLUE_GREY_900
                              ,content=ft.Row(
                                   alignment='center',
                                   expand=True,
                                  controls=[
                                      ft.IconButton(ft.icons.HOME,icon_size=40)
                                      ,ft.IconButton(ft.icons.COFFEE,icon_size=40)
                                      ,ft.IconButton(ft.icons.SETTINGS, icon_size=40)
                                  ]
                              )
                              )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    login=ft.Container(
        expand=True,
        visible=True,
        content=ft.Column(
            expand=True
            ,controls=[
                ft.Container(
                    height=250,
                    border_radius=10
                    ,bgcolor=ft.colors.BLACK
                    ,alignment=ft.alignment.center
                    ,content=ft.Image(src='../assets/robot.svg',color=ft.colors.BLUE_900,height=225)      
                ),
                
                ft.Container(
                    alignment=ft.alignment.center
                    ,expand=True
                    ,bgcolor=ft.colors.BLUE_GREY_900
                    ,padding=25
                    ,content=ft.Column(#
                            alignment=ft.alignment.center,
                            horizontal_alignment=ft.alignment.center
                            ,expand=True
                            ,controls=[
                                ft.Container(
                                    content=ft.Text(
                                    'Iniciar Sesión'
                                     ,size=30
                                     ,width=320
                                     ,text_align="center"
                                     ,weight=ft.FontWeight.W_900
                                    ),
                                    padding=ft.padding.only(20,20)
                                )
                                ,email
                                ,password
                                ,ft.ElevatedButton(text='Login', on_click=lambda e: login_registrer(0),width=310)
                                ,ft.Container(
                                    padding=20
                                    ,content=ft.Row(
                                        controls=[
                                            ft.Text('¿No tienes cuenta?',size=18),
                                            ft.TextButton(text='Regístrate', on_click=lambda e: login_registrer(1),)
                                        ]
                                        ,alignment=ft.alignment.center
                                    ),
                                )
                            ]
                        )
                    )
            ]
        )
    )
    
    contenedor=ft.Container(
        expand=True
        ,content=ft.Stack(
            expand=True
            ,controls=[
                container,
                login
            ]
        )
    )
    
    # agregar componentes a la página
    page.add(contenedor)



# función principal
ft.app(target=main,assets_dir='../assets')