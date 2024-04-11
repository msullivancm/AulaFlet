from os import link
from re import T
from tracemalloc import stop
from turtle import bgcolor, color
from click import style
import flet as ft
import math

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50
    
    #para dicas de gradient - hypercolor.dev | uigradients.com
    
    elementos = [
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                colors=[
                    ft.colors.CYAN,
                    ft.colors.AMBER,
                    ft.colors.PURPLE,
                ],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                stops=[0, 0.3, 1], 
                rotation=math.radians(45),
            ),
        ),
        ft.Container(
            expand=True,
            gradient=ft.RadialGradient(
                colors=[
                    ft.colors.AMBER,
                    ft.colors.ORANGE,
                    ft.colors.DEEP_ORANGE,
                    ft.colors.RED,
                ],
                stops=[0, 0.4, 0.8, 1],
                center=ft.Alignment(0.5, 0.5),
                radius=1,
            ),
        ),
        ft.Container(
            expand=True,
            gradient=ft.SweepGradient(
                colors=[
                    ft.colors.AMBER,
                    ft.colors.BLACK,
                    ft.colors.RED,
                ],
                stops = [0, 0.5, 1],
                center=ft.Alignment(0,0.7),
                rotation=math.radians(90),
            ),
        )
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')