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
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    elementos = [
        ft.Container(
            # height=100,
            # width=100,
            bgcolor="grey",
            image_src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            expand=True,
            margin=ft.margin.all(20),
            border=ft.border.all(5, color=ft.colors.RED),
            border_radius=20,
            content=ft.Row(
                [
                    ft.ElevatedButton(text="Texto 1"),
                ],
            ),
            alignment=ft.alignment.center,
            #padding=ft.padding.all(40),
            
            shape=ft.BoxShape.CIRCLE ,
            
            gradient=ft.LinearGradient(
                colors=[ft.colors.AMBER, ft.colors.RED],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            shadow=ft.BoxShadow(
                spread_radius=10,
                blur_radius=50,
                color=ft.colors.RED,
                #offset=ft.Offset(10, 10),
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        )
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir="assets")
