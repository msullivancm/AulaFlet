from os import link
from re import T
from textwrap import wrap
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
    
    elementos = [
        ft.ResponsiveRow(
            columns=12, # Número de colunas
            controls=[
                ft.TextButton(
                    text='Excluir',
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED,
                    tooltip='Excluir',
                    #url='https://www.google.com',
                    style=ft.ButtonStyle(color=ft.colors.RED), 
                    on_click=lambda e: print('Excluir'),
                    col=4, # Número de colunas que o botão irá ocupar
                ),
                ft.TextButton(
                    text='Editar',
                    icon=ft.icons.EDIT,
                    icon_color=ft.colors.BLUE,
                    tooltip='Editar',
                    #url='https://www.google.com',
                    style=ft.ButtonStyle(color=ft.colors.RED), 
                    on_click=lambda e: print('Editar'),
                ),
                ft.TextButton(
                    text='Excluir',
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED,
                    tooltip='Excluir',
                    #url='https://www.google.com',
                    style=ft.ButtonStyle(color=ft.colors.RED), 
                    on_click=lambda e: print('Excluir'),
                ),
            ],
        ),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')