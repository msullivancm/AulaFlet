import time

import flet as ft

class Product(ft.UserControl):
    def __init__(self, image: str, title: str):
        super().__init__()
        self.image = image
        self.title = title

    def build(self):
        return ft.Container(
            image_src=self.image,
            image_fit=ft.ImageFit.COVER,
            height=500,
            aspect_ratio=1.0,
            alignment=ft.alignment.bottom_center,
            padding=ft.padding.all(20),
            content=ft.Text(
                value=self.title,
                size=30,
                #color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
            )
        )

    def did_mount(self):
        print('Product did mount '+self.title)

    def will_unmount(self):
        print('Product will unmount '+self.title)

    def destroy(self):
        print('Product destroy '+self.title)
        self.will_unmount()
        self.clean()
def main(page: ft.Page):
    page.scroll=ft.ScrollMode.AUTO
    page.window_width = 400.0
    page.window_height = 800
    page.add(
        prod1 := Product(
            image='assets/icons/icon-512.png',
            title='Product 1',
        )
    )

    time.sleep(4)

    page.add(
        prod2 := Product(
            image='assets/icons/icon-maskable-512.png',
            title='Product 2',
        ),
    )

    time.sleep(4)

    prod1.destroy()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')