from os import link
from re import T
from turtle import bgcolor, color
from click import style
import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50
    
    style = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.RED,
        },
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.AMBER,
            '': ft.colors.BLUE,
        },
        padding={
            ft.MaterialState.HOVERED: 30,
            ft.MaterialState.DEFAULT: 20,
        }, 
        animation_duration=1000,
        side={
            ft.MaterialState.HOVERED: ft.BorderSide(color=ft.colors.RED, width=2),
            ft.MaterialState.DEFAULT: ft.BorderSide(color=ft.colors.BLUE, width=2)
        },
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
            ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=10)
        }
    )
    
    elementos = [
        ft.ElevatedButton(text='Elevated Button'),
        ft.ElevatedButton(text='Botão inativo', disabled=True),
        ft.ElevatedButton(text='Botão com tooltip', tooltip='Clique aqui'),
        ft.ElevatedButton(text='Botão com ícone', icon=ft.icons.FAVORITE_OUTLINE),
        ft.ElevatedButton(text='Botão com ícone colorido e tooltip', 
                          bgcolor=ft.colors.GREEN,
                          color=ft.colors.WHITE,
                          icon_color=ft.colors.RED,
                          icon=ft.icons.FAVORITE_OUTLINE, 
                          tooltip='Clique aqui',
                          url='https://www.google.com',
                          ),
        ft.ElevatedButton(text='Botão com estilo personalizado', 
                         style=style,
                         tooltip='Clique aqui',
                         url='https://www.google.com'),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')