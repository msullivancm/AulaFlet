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
    
    elementos = [
        
    ]
    
    page.add(*elementos)

# Só executa este código se este arquivo for o principal
if __name__ == "__main__":
    ft.app(target=main)