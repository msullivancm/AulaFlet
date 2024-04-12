import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    av1 = ft.CircleAvatar(
        foreground_image_url='https://i.imgur.com/erNQ3i8.jpeg',
        radius=50,
        tooltip='Avatar 1',
    )

    elementos = [
        av1,
        av2 := ft.CircleAvatar(
            bgcolor=ft.colors.AMBER,
            color=ft.colors.WHITE,
            content=ft.Text(value='PA'),
            max_radius=200,
            min_radius=100,
            tooltip='Avatar 2',
        ),
        av3 := ft.Badge(
            content=av1,
            bgcolor=ft.colors.GREEN,
            #small_size=100,
            text='3',
        )
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')