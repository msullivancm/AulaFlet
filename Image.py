from os import link
from re import T
import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    img = ft.Image(
        src='image\python.jpeg',
        height=400,
        width= 400,
        border_radius=ft.border_radius.all(10),
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.REPEAT,
        tooltip='Logo do python',
    )
    
    img2 = ft.Image(
        src='image\python.jpeg',
        height=400,
        width= 400,
        border_radius=ft.border_radius.all(10),
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        tooltip='Imagem de uma cobra',
    )
    
    page.add(img, img2)

ft.app(target=main, assets_dir='assets')