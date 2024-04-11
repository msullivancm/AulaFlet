from os import link
from re import T
import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    page.fonts = {
        'Kanit': 'github.com/google/fonts/blob/main/ofl/kanit/Kanit-Regular.ttf?raw=true',
        'Dragon Slayer': 'fonts\Dragon Slayer.ttf',
    }
    
    t1 = ft.Text(
        value='Hello World!', 
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.RED,
        color = ft.colors.WHITE,
        font_family='Dragon Slayer',
        )
    
    t2 = ft.Text(
        value='Hello World!', 
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.RED,
        color = ft.colors.WHITE,
        font_family='Kanit',
        no_wrap=True,
        )
    
    t3 = ft.Text(
        value='Hello World!', 
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.RED,
        color = ft.colors.WHITE,
        italic = True,
        max_lines= 5,
        overflow=ft.TextOverflow.ELLIPSIS,
        selectable=True,
        size=20,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_400,
        )

    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    title_style = ft.TextStyle(font_family='Kanit', 
                               size=30, 
                               weight=ft.FontWeight.W_700, 
                               color=ft.colors.AMBER, 
                               bgcolor=ft.colors.BLUE, 
                               decoration_color=ft.colors.RED,
                               decoration_thickness=2.0,
                               decoration_style=ft.TextDecorationStyle.DOUBLE,
                               decoration=ft.TextDecoration.OVERLINE,)
    t4 = ft.Text(
        value='texto com link', 
        spans=[
            ft.TextSpan(text='Texto sem link ', style=link_style), 
            ft.TextSpan(text='texto intermediário'),
            ft.TextSpan(text='Texto com link', url='https://www.google.com.br', style=link_style),
            ft.TextSpan(text=' texto final', style=title_style),
        ],
        size = 40,
        )
    
    page.add(t1, t2, t3, t4)

ft.app(target=main)