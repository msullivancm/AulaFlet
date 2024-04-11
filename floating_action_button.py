from json import tool
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
    page.spacing = 50

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREEN,
        mini=True,
        shape=ft.CircleBorder(),
        tooltip="Adicionar",
        # text='Adicionar',
        on_click=lambda _: print("Adicionar"),
    )

    page.update() 
    
    page.add(
        ft.Container(
            content=ft.FloatingActionButton(text="Botão Personalizado", 
                                            on_click=lambda _: print("Botão Personalizado"), 
                                            width=100),
            bgcolor=ft.colors.BLUE,
            height=400,
            alignment=ft.Alignment(x=1, y=-1),
        )
    )


ft.app(target=main, assets_dir="assets")
