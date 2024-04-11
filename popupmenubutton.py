from os import link
from re import T
from tabnanny import check
from turtle import bgcolor, color
from click import style
import flet as ft


def main(page: ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def item4_click(e):
        e.control.checked = not e.control.checked
        e.control.update()
        
    elementos = [
        ft.PopupMenuButton(
            icon=ft.icons.MENU_BOOK,
            items=[
                ft.PopupMenuItem(
                    text="Item 1",
                    icon=ft.icons.CHECK,
                    on_click=lambda e: print("Item 1"),
                ),
                ft.PopupMenuItem(
                    text="Item 2",
                    icon=ft.icons.CHECK,
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.NOTIFICATION_IMPORTANT),
                            ft.Column(
                                [ft.Text("Item 2"), ft.Text("Subtitulo do item 2")]
                            ),
                        ]
                    ),
                    on_click=lambda e: print("Item 2"),
                ),
                ft.PopupMenuItem(),
                ft.PopupMenuItem(
                    text="Item 3",
                    icon=ft.icons.CHECK,
                    on_click=lambda e: print("Item 3"),
                ),
                ft.PopupMenuItem(
                    text="Item 4",
                    icon=ft.icons.SELECT_ALL,
                    on_click=item4_click,
                    checked=False,
                ),
            ],
        )
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir="assets")
