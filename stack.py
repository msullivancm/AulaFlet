import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50

    layout = ft.Stack(
        controls=[
            ft.Container(
                image_src='https://picsum.photos/600/800',
                image_fit=ft.ImageFit.COVER,
            ),
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.colors.TEAL,ft.colors.CYAN]
                ),
                opacity=0.8,
            ),
            ft.Text(value='Título', top=0, left=0),
            ft.Column(controls=[
                ft.Text(value='Corpo'),
            ],
            top=50, left=0),
        ]
    )

    elementos = [
        layout,
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
