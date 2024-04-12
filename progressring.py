import time

import flet as ft


def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50

    elementos = [
        pr := ft.ProgressRing(
            value=0.0,
            color=ft.colors.RED,
            scale=2.0,
        ),
    ]

    page.add(*elementos)

    # Simulate progress
    while True:
        if pr.value >= 0.1 and pr.value < 1.0:
            pr.value += 0.1
        else:
            pr.value = 0.1
        time.sleep(1)
        page.update()

ft.app(target=main, assets_dir='assets')