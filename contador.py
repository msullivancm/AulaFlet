from os import link
from re import T
from turtle import bgcolor, color
from click import style
import flet as ft


def main(page: ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 5

    page.title = "Contador"
    
    texto = ft.Text(value="0", style=ft.TextThemeStyle.TITLE_LARGE)

    def mais(e): 
        texto.value = str(int(texto.value) + 1)
        texto.update()

    def menos(e): 
        texto.value = str(int(texto.value) - 1)
        texto.update()
    
    elementos = [
        ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(icon=ft.icons.REMOVE, on_click=menos),
                    texto,
                    ft.IconButton(icon=ft.icons.ADD, on_click=mais),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.GREY,
        ),
    ]
    
    
    page.add(*elementos)


ft.app(target=main, assets_dir="assets")
