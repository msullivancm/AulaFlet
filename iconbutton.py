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
    
    def play_pause(e):
        e.control.selected = not e.control.selected
        e.control.update()
    
    elementos = [
        ft.IconButton(
            icon=ft.icons.DELETE_FOREVER_ROUNDED,
            bgcolor=ft.colors.GREEN,
            tooltip="delete",
            icon_color=ft.colors.RED,
            icon_size=30,
        ),
        ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE,
            selected_icon=ft.icons.PAUSE_CIRCLE,
            selected=False,
            tooltip="Play",
            icon_color=ft.colors.RED,
            icon_size=150,
            on_click=play_pause,
            style=ft.ButtonStyle(
                color={ 
                    ft.MaterialState.SELECTED: ft.colors.GREEN,
                    ft.MaterialState.DEFAULT: ft.colors.BLUE,
                }
            ),
        ),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')