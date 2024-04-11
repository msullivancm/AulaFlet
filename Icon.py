from os import link
from re import T
import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    icon1 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.RED, size=50)
    icon2 = ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.BLUE, size=80, tooltip='Música')
    icon3 = ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.GREEN, size=50)
    icon4 = ft.Icon(name='settings', color=ft.colors.AMBER, size=150, tooltip='Configurações')
    
    page.add(icon1, icon2, icon3, icon4)

ft.app(target=main, assets_dir='assets')