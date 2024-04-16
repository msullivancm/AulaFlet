import flet as ft


def main(page: ft.Page):
    page.window_width = 750.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50
    page.bgcolor = ft.colors.BLACK

    def expand_image(e):
        for c in carousel.controls:
            c.col = 1
        e.control.col = 12 - len(carousel.controls) + 1
        carousel.update()

    carousel = ft.ResponsiveRow(
        columns=12,
        spacing=5,
        controls=[
            ft.Container(
                col=1,
                image_src=f'https://picsum.photos/250/300?{i}',
                image_fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(5),
                on_click=expand_image,
            ) for i in range(10, 18)
        ]
    )

    carousel.controls[0].col = 12 - len(carousel.controls) + 1

    layout = ft.Container(
        width=700,
        height=300,
        bgcolor=ft.colors.GREY_200,
        shadow=ft.BoxShadow(blur_radius=500, color=ft.colors.AMBER),
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=carousel
    )

    elementos = [
        layout,
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
