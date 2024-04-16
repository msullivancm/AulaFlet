import math

import flet as ft
import itertools


class AnimatedContainer(ft.UserControl):
    cores = itertools.cycle(['AMBER', 'BLUE', 'CYAN'])

    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs

    def build(self):
        return ft.Container(
            width=200,
            height=200,
            bgcolor=next(AnimatedContainer.cores),
            opacity=1,
            offset=ft.transform.Offset(x=0, y=0),
            rotate=ft.transform.Rotate(angle=0, alignment=ft.alignment.bottom_right),
            scale=ft.transform.Scale(scale=1),
            animate=ft.animation.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN_OUT),
            animate_opacity=True,
            animate_offset=True,
            animate_scale=True,
            animate_rotation=True,
            **self.kwargs
        )


def main(page: ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def animate_opacity(e):
        e.control.opacity = 0.1 if e.control.opacity == 1 else 1
        e.control.update()

    def animate_offset(e):
        e.control.offset.x = 0.5 if e.control.offset.x == 0 else 0
        # e.control.offset.y = 0.1 if e.control.offset.y == 0 else 0
        e.control.update()

    def aminate_rotation(e):
        e.control.rotate.angle = math.radians(45) if e.control.rotate.angle == 0 else 0
        e.control.update()

    def animate_scale(e):
        e.control.scale.scale = 0.5 if e.control.scale.scale == 1 else 1
        e.control.update()

    def animate_position(e):
        e.control.top = 20 if e.control.top == 0 else 0
        e.control.left = 0 if e.control.left == 400 else 0
        e.control.update()

    elementos = [
        ft.Column(
            controls=[
                AnimatedContainer(on_hover=animate_opacity),
                AnimatedContainer(on_hover=animate_offset),
                AnimatedContainer(on_hover=aminate_rotation),
                AnimatedContainer(on_hover=animate_scale),
                AnimatedContainer(
                    top=0,
                    left=400,
                    animate_position=True,
                    on_click=animate_position
                )
            ]
        )
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
