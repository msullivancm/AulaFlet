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
    
    page.theme = ft.Theme(
            text_theme=ft.TextTheme(
            title_large = ft.TextStyle(size=30, weight=ft.FontWeight.W_900),
            ),
            color_scheme=ft.ColorScheme(
                primary=ft.colors.PINK,
                secondary=ft.colors.RED,
                background=ft.colors.GREEN,
                on_primary=ft.colors.WHITE,
                on_secondary=ft.colors.WHITE,
                on_background=ft.colors.BLACK,
            ),
    )
    
    theme = ft.Theme(
            text_theme=ft.TextTheme(
            title_large = ft.TextStyle(size=30, weight=ft.FontWeight.W_900),
            ),
            color_scheme=ft.ColorScheme(
                primary=ft.colors.BLUE,
                secondary=ft.colors.AMBER,
                background=ft.colors.GREY,
                on_primary=ft.colors.WHITE,
                on_secondary=ft.colors.WHITE,
                on_background=ft.colors.BLACK,
            ),
    )

    elementos = [
        ft.Container(
            height=100,
            width=200,
            padding=10,
            content=ft.Column(
                [
                    ft.Text(value="Tema 1", style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text="Botão 1", color=ft.colors.AMBER),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        ),
        ft.Container(
            height=100,
            width=200,
            padding=10,
            content=ft.Column(
                [
                    ft.Text(value="Tema 2", style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text="Botão 1", color=ft.colors.AMBER),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
            theme=theme,
        )
    ]

    page.add(*elementos)
    
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.CHANGE_CIRCLE,
        shape=ft.RoundedRectangleBorder(radius=100),
        on_click=change_theme,
        mini=True,
    )
    
    page.update()

ft.app(target=main, assets_dir="assets")
