import flet as ft


def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    with open('./markdown.md', 'r') as f:
        markdown = f.read()

    elementos = [
        coluna := ft.Column([
            md1 := ft.Markdown(
                value=markdown,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link=lambda e: page.launch_url(e.data),
                code_theme='monokai-sublime'
            ),
            separator := ft.Markdown(value='---'),
            md2 := ft.Markdown(
                value="""
                # Este é o título
                ### Este é o subtítulo
                - item 1
                - item 2

                ** Texto em negrito **
                _Texto em itálico_
                """
            )
        ],
            expand=True,
            scroll=True,
            spacing=20,
            auto_scroll=True
        ),

    ]

    page.add(*elementos)


ft.app(target=main, assets_dir='assets')
