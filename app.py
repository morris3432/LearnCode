# libs
import flet as ft 
from werkzeug.security import generate_password_hash, check_password_hash
# models
from models.Users_Models import Uesrs_Models
from models.levls_models import levels_models
from components.card import Cart   
 
def main(page: ft.Page):
    page.window.height = 800
    page.window.width = 380
    page.window.resizable = False
    page.theme = ft.Theme(color_scheme_seed="blue")
    
    # conectar a MongoDB
    db=Uesrs_Models()
    model=levels_models()
    niveles=model.get_levels()
    carts=Cart()
    
    def advertisement(e):
        page.close(advert)
        
    def  theme (e):
        if contenedor.bgcolor == 'black':
            contenedor.bgcolor='white'
            buthontheme.icon=ft.icons.DARK_MODE
        elif contenedor.bgcolor == 'white':
            contenedor.bgcolor='black'
            buthontheme.icon=ft.icons.LIGHT_MODE
        page.update()
        
    def login_registrer(e):
        nom=str(email.value)
        passwords=str(password.value)
        passwordC=str(passwordconfirm.value)
        user_name=str(nombre.value)
        
        if e == 0: # login
            user=db.find_user(nom)
            if not user:
                error.value='Usuario no encontrado'
            elif check_password_hash(user['password'],passwords):
                container.visible = True
                login.visible=False
                nn=user['user_name']
                em=user['email']
                nombreu.value=nn
                emailu.value=em
                advert.content=ft.Text(f'bienvenido {nn} a Learn Code')
                page.open(advert)
            else:
                error.value='Contraseña incorrecta'
                email.value=''
                password.value=''
            page.update()
        elif e == 1:
            if passwords!= passwordC:
                print('Contraseñas no coinciden')
            elif db.find_user(user_name):
                print('Nombre de usuario ya utilizado')
            else:
                db.insert_user(user_name,nom, generate_password_hash(passwords))
                print('Usuario registrado')
                email.value=''
                password.value=''
                passwordconfirm.value=''
                nombre.value=''
                    
    def change_in(e):
        inicio.visible=False
        seting.visible=False
        levels.visible=False
        if e == 0:
            inicio.visible=True
            levels.visible=False
            seting.visible=False
        elif e == 1:
            seting.visible=False
            levels.visible=True
            inicio.visible=False
        elif e == 2:
            inicio.visible=False
            seting.visible=True
            levels.visible=False
        page.update()
            
    def chang_log(e):
        loginform.visible=False
        registerform.visible=True
        
        if e == 0:
            loginform.visible=False
            registerform.visible=True
        elif e == 1:
            loginform.visible=True
            registerform.visible=False
        page.update()
    
    advert = ft.AlertDialog(
            modal=True,
            title=ft.Text("Bienvenido ", size=20, weight=ft.FontWeight.W_900),
            actions=[
                ft.TextButton("Aceptar", on_click=advertisement),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
    )
    error=ft.Text(value='',color='red',weight=ft.FontWeight.W_300)
    nombre=ft.TextField(
        hint_text='Nombre de usuario'
        ,border='underline'
        ,color='blue'
        ,prefix_icon=ft.icons.PERSON
    )
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
    passwordconfirm=ft.TextField(
        hint_text='Confirmar Contraseña'
        ,border='underline'
        ,color='blue'
        ,prefix_icon=ft.icons.LOCK
        ,password=True
        ,can_reveal_password= True
    )
    
    nombreu=ft.Text(value='',size=20,weight=ft.FontWeight.W_900,width=300,text_align='center')
    emailu=ft.Text(value='',size=15,weight=ft.FontWeight.W_500,width=300,text_align='center')
    id=ft.Text(value='',size=0 ,weight=ft.FontWeight.W_900,width=300,text_align='center')
    
    inicio=ft.Container(
        visible=True
        ,expand=True
        ,bgcolor=ft.colors.LIGHT_BLUE_900
        
    )
    
    buthontheme=ft.TextButton(icon=ft.icons.LIGHT_MODE,text='Tema',on_click=theme)
    
    seting=ft.Container(
        visible=False
        ,expand=True
        ,padding=25
        ,content=ft.Column(
            expand=True
            ,controls=[
                ft.Container(
                    alignment=ft.alignment.center
                    ,content=ft.Image(src='../assets/foto.jpeg',border_radius=10,height=100,width=100)
                ),
                ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[
                        nombreu,
                        emailu
                    ]
                )
                )
                ,buthontheme
            ]
        )
    )
    
    cards=[
        carts.create_card(nivel)
        for nivel in niveles
    ]

    levels=ft.Container(
        visible=False
        ,expand=True
        ,content=ft.Column(
            expand=True,
            scroll='auto',
            controls=[
                ft.Row(
                    col=12,
                    controls=cards
                )
            ]
        )
    )
    
    loginform=ft.Container(
                    alignment=ft.alignment.center
                    ,expand=True
                    ,bgcolor=ft.colors.BLUE_GREY_900
                    ,padding=ft.padding.only(20,55,20)
                    ,visible=True
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
                                ,error
                                ,ft.ElevatedButton(text='Login', on_click=lambda e: login_registrer(0),width=310)
                                ,ft.Container(
                                    padding=20
                                    ,content=ft.Row(
                                        controls=[
                                            ft.Text('¿No tienes cuenta?',size=18),
                                            ft.TextButton(text='Regístrate', on_click=lambda e: chang_log(0),)
                                        ]
                                        ,alignment=ft.alignment.center
                                    ),
                                )
                            ]
                        )
                    )
    
    registerform=ft.Container(
                    alignment=ft.alignment.center
                    ,expand=True
                    ,bgcolor=ft.colors.BLUE_GREY_900
                    ,padding=25
                    ,visible=False
                    ,content=ft.Column(#
                            alignment=ft.alignment.center,
                            horizontal_alignment=ft.alignment.center
                            ,expand=True
                            ,controls=[
                                ft.Container(
                                    content=ft.Text(
                                    'Crea tu cuenta'
                                     ,size=30
                                     ,width=320
                                     ,text_align="center"
                                     ,weight=ft.FontWeight.W_900
                                    ),
                                    padding=ft.padding.only(20,20)
                                )
                                ,nombre
                                ,email
                                ,password
                                ,passwordconfirm
                                ,ft.ElevatedButton(text='Crear', on_click=lambda e: login_registrer(1),width=310)
                                ,ft.Container(
                                    padding=20
                                    ,content=ft.Row(
                                        controls=[
                                            ft.Text('¿Ya tienes cuenta?',size=18),
                                            ft.TextButton(text='Iniciar sesión', on_click=lambda e: chang_log(1),)
                                        ]
                                        ,alignment=ft.alignment.center
                                    ),
                                )
                            ]
                        )
                    )
    
            
    container = ft.Container(
        visible=False,
        width=350,
        height=745,
        padding=5,
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Stack(
                    expand=True
                    ,controls=[
                        inicio
                        ,levels
                        ,seting
                    ]
                )
                ,ft.Container(border_radius=8 ,height=50,bgcolor=ft.colors.BLUE_GREY_900
                              ,content=ft.Row(
                                   alignment='center',
                                   expand=True,
                                  controls=[
                                      ft.IconButton(ft.icons.HOME,icon_size=40,on_click=lambda e:change_in(0))
                                      ,ft.IconButton(ft.icons.COFFEE,icon_size=40, on_click=lambda e: change_in(1))
                                      ,ft.IconButton(ft.icons.SETTINGS, icon_size=40,on_click=lambda e: change_in(2))
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
                ft.Stack(
                    expand=True
                    ,controls=[
                        loginform,
                        registerform
                    ]
                )  
            ]
        )
    )
    
    contenedor=ft.Container(
        expand=True
        ,bgcolor='black'
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
ft.app(target=main,assets_dir='assets')