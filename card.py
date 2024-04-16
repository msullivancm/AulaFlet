import flet as ft


def main(page: ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    card = ft.Card(content=ft.Column(controls=[
        ft.Text('Card Title', style=ft.TextThemeStyle.TITLE_LARGE),
        ft.Text('Card Description', style=ft.TextThemeStyle.TITLE_SMALL),
        ft.FilledButton('Salvar'),
    ]),
        color=ft.colors.GREY_900,
        width=200,
        height=150,
        elevation=5,)

    elementos = [
        card,
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
