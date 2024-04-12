import flet as ft


def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def opcao(num: int):
        return ft.dropdown.Option(num, f'opcao{num}')

    elementos = [
        ft.Dropdown(
            options=[
                opcao(num) for num in range(1,5)
            ],
            value=2,
            label='Escolha uma opção',
            on_change=lambda e: print(e.control.value)
        )
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir='assets')
