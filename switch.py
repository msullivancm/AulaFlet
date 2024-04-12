from os import link
from re import T
from turtle import bgcolor, color
from click import style
import flet as ft


def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def mudar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    elementos = [
        ft.Switch(label='Mudar Thema', on_change=mudar_tema),
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir='assets')