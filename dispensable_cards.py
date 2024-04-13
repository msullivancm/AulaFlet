import flet as ft

#gerar compilações
##para windows
#flet build windows --module-name .\dispensable_cards.py --project "Marvel Cards"
##para web
#flet build web --module-name .\dispensable_cards.py --project "Marvel Cards"
##para android
#flet build apk --module-name .\dispensable_cards.py --project "Marvel Cards"

def main(page: ft.Page):
    # page.window_top = 0
    # page.window_left = 2120.0
    # page.window_width = 450
    # page.window_height = 1000

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50

    page.bgcolor = ft.colors.WHITE

    images = [
        'https://github.com/msullivancm/AulaFlet/blob/52a04b17053db3141b044aa0b7d79f9c30fe7804/assets/images/poster1.jpg',
        'https://github.com/msullivancm/AulaFlet/blob/52a04b17053db3141b044aa0b7d79f9c30fe7804/assets/images/poster2.jpg',
        'https://github.com/msullivancm/AulaFlet/blob/52a04b17053db3141b044aa0b7d79f9c30fe7804/assets/images/poster3.jpg',
        'https://github.com/msullivancm/AulaFlet/blob/52a04b17053db3141b044aa0b7d79f9c30fe7804/assets/images/poster4.jpg',
        'https://github.com/msullivancm/AulaFlet/blob/52a04b17053db3141b044aa0b7d79f9c30fe7804/assets/images/poster5.jpg',
        'assets/images/poster6.jpg',
        'assets/images/poster7.jpg',
        'assets/images/poster8.jpg',
    ]

    def change_posters():
        for poster in posters.controls:
            poster.content.offset.x += poster.data * 0.2
            poster.content.scale.scale -= poster.data * 0.1
            poster.content.opacity -= poster.data * 0.3
        posters.update()

    def handle_dismiss(e):
        for num, poster in enumerate(posters.controls):
            if e.control == posters.controls[0]:
                posters.controls.clear()
                posters.controls.extend([
                    ft.Dismissible(
                        content=ft.Container(
                            image_src=img,
                            border_radius=ft.border_radius.all(10),
                            image_fit=ft.ImageFit.COVER,
                            aspect_ratio=9 / 16,
                            offset=ft.Offset(0, 0),
                            scale=ft.Scale(1, 1),
                            opacity=1,
                            shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                            animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                            animate_offset=True,
                            animate_opacity=True,
                            animate_scale=True,
                        ),
                        data=pos,
                        on_dismiss=handle_dismiss,
                    ) for pos, img in reversed(list(enumerate(images)))
                    # enumerate() returns a tuple with the index and the element. reversed() returns the list in reverse order.
                ])
                break
            poster.data -= 1
            poster.content.offset.x = 0
            poster.content.opacity = 1
            poster.content.scale.scale = 1
        change_posters()

    posters_list = [
        ft.Dismissible(
            content=ft.Container(
                image_src=img,
                border_radius=ft.border_radius.all(10),
                image_fit=ft.ImageFit.COVER,
                aspect_ratio=9 / 16,
                offset=ft.Offset(0, 0),
                scale=ft.Scale(1, 1),
                opacity=1,
                shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                animate_offset=True,
                animate_opacity=True,
                animate_scale=True,
            ),
            data=pos,
            on_dismiss=handle_dismiss,
        ) for pos, img in reversed(list(enumerate(images)))
        # enumerate() returns a tuple with the index and the element. reversed() returns the list in reverse order.
    ]

    posters = ft.Stack(
        height=500,
        controls=posters_list,
    )

    layout = ft.Row(controls=[posters], alignment=ft.MainAxisAlignment.CENTER)

    elementos = [
        layout,
    ]

    page.add(*elementos)

    change_posters()


ft.app(target=main, assets_dir='assets')
