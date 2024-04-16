import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50
    
    elementos = [
        tp:=ft.Tooltip(
            content=ft.Text('Tooltip'),
            message='Eu sou um tooltip',
            bgcolor=ft.colors.AMBER,
            border=ft.border.all(5, ft.colors.RED),
            border_radius=ft.border_radius.all(10),
            height=100,
            margin=ft.margin.all(10),
            padding=ft.padding.all(10),
            text_align=ft.TextAlign.RIGHT,
            text_style=ft.TextStyle(italic=True, color=ft.colors.WHITE),
            wait_duration=300,
            gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=[ft.colors.RED, ft.colors.BLUE]),
        )
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
