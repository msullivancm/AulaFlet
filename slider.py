import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50

    # def printar_valor(e):
    #     print('Selecionado:', e.control.value)

    elementos = [
        ft.Slider(
            min=0,
            max=100,
            value=50,
            divisions=10,
            label='Slider {value}',
            on_change = lambda e: print('Selecionado:', e.control.value)
        ),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')