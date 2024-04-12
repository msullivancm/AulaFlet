from os import link
from re import T
from turtle import bgcolor, color
from click import style
import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50   
    
    def image(num: int):
        return ft.Image(
                src=f'https://picsum.photos/150/150?{num}',
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
            )
    
    def page_resize(e):
        print('Page resized', page.window_width, page.window_height, page.window_top, page.window_left)
    page.on_resize = page_resize
    
    def alterna_entre_colunas(e):
        btn1.style = btn_style_unselected
        btn2.style = btn_style_unselected
        e.control.style = btn_style_selected
        print(e.control.text)
        if e.control.text == 'Todas as Fotos':
            layout.controls[0] = grid1
        else:
            layout.controls[0] = grid2
        page.update()
         
    grid1 = ft.GridView(
        controls=[
            image(num) for num in range(60)
        ],
        expand=True,
        runs_count=3,
        max_extent=150,
        child_aspect_ratio=1.0,
    )
    
    grid2 = ft.Column(
        controls=[
            ft.Text(value='2024', size=30),
            ft.GridView(
                controls=[
                    image(num) for num in range(1,20)
                ],
                expand=True,
                runs_count=3,
                max_extent=150,
                child_aspect_ratio=1.0,
            ),
            ft.Text(value='2023', size=30),
            ft.GridView(
                controls=[
                    image(num) for num in range(21,40)
                ],
                expand=True,
                runs_count=3,
                max_extent=150,
                child_aspect_ratio=1.0,
            ),
            ft.Text(value='2022', size=30),
            ft.GridView(
                controls=[
                    image(num) for num in range(40,60)
                ],
                expand=True,
                runs_count=3,
                max_extent=150,
                child_aspect_ratio=1.0,
            )
        ],
        expand=True,
    )
    
    btn_style_selected = ft.ButtonStyle(
        bgcolor='blue',
        color='white',
        overlay_color='purple',
    )
    
    btn_style_unselected = ft.ButtonStyle(
        bgcolor='white',
        color='black',
        overlay_color='grey',
    )
    
    footer = ft.Container(
        content=ft.Row(
                controls=[
                btn1 := ft.ElevatedButton(text='Todas as Fotos', on_click=alterna_entre_colunas, style=btn_style_selected),
                btn2 := ft.ElevatedButton(text='Agrupadas', on_click=alterna_entre_colunas, style=btn_style_unselected),
                ]
            )
    )
    
    layout = ft.Column(
            expand=True,
            controls=[ 
                      grid1,
                      footer
                      ]
        )
    
    page.add(layout)

ft.app(target=main, assets_dir='assets')