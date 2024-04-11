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

    elementos = [
        ft.OutlinedButton(
            text="Outlined Button",
            icon=ft.icons.ZOOM_IN,
            icon_color=ft.colors.RED,
            tooltip="Zoom In",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=20),
            ),
        ),
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir="assets")
