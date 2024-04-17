import flet as ft
from typing import List

class Carousel(ft.UserControl):
    def __init__(self, controls: List[ft.Control], height: int = 250, **kwargs):
        super().__init__(**kwargs)
        self.carousel = ft.Row(
            height=height,
            scroll=ft.ScrollMode.HIDDEN,
            controls=controls
        )

    def move_backward(self, e):
        self.carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        self.carousel.update()

    def move_forward(self, e):
        self.carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        self.carousel.update()

    def build(self):
        return ft.Column(
            controls=[
                self.carousel,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_LEFT,
                            on_click=self.move_backward
                        ),
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT,
                            on_click=self.move_forward
                        )
                    ]
                )
            ]
        )