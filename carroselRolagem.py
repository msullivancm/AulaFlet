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
    page.bgcolor = ft.colors.WHITE

    def move_backward(e):
        carousel.scroll_to(delta=-200, duration=300,curve=ft.AnimationCurve.DECELERATE),
        carousel.update()

    def move_forward(e):
        carousel.scroll_to(delta=200, duration=300,curve=ft.AnimationCurve.DECELERATE),
        carousel.update()

    layout = ft.Container(
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}',
                        ) for num in range(10)
                    ],
                    scroll=ft.ScrollMode.HIDDEN,
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            ]
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.GREY),
    )

    elementos = [
        layout,
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
