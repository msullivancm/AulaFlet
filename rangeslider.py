import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50

    elementos = [
        rs := ft.RangeSlider(
            start_value=20,
            end_value=80,
            min=0,
            max=100,
            divisions=10,
            label='Slider {value}',
            round=2,
            on_change=lambda _: print(rs.start_value, '->', rs.end_value),
        ),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')