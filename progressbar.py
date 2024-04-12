import time

import flet as ft

def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    pb1 = ft.ProgressBar(
        value=0.1,
        bar_height=50,
        color=ft.colors.RED,
        bgcolor=ft.colors.GREEN,
        tooltip='Barra de Progresso',
    )

    elementos = [
        pb1,
        pb2 := ft.ProgressBar(
            bar_height=50,
        ),
    ]

    page.add(*elementos)

    for i in range(10):
        pb1.value += 0.1
        time.sleep(1)
        page.update()

ft.app(target=main, assets_dir='assets')