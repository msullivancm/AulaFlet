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
        ft.GridView(
            [
                ft.Image(src=f"https://picsum.photos/250/300?{num}", fit="cover")
                for num in range(20)
            ],
            #runs_count=2,
            spacing=20,
            run_spacing=20,
            padding=10,
            max_extent=200,
            expand=True,
            auto_scroll=True,
            child_aspect_ratio=1.77, #imagem 16/9 = 1.77 
            #child_aspect_ratio=0.56, #imagem 9/16 = 0.56
            
        ),
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir="assets")
