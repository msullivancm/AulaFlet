import flet as ft


def main(page: ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def edita_view(e):
        view.value = e.control.value
        view.update()

    editor = ft.TextField(
        multiline=True,
        min_lines=30,
        max_lines=30,
        color=ft.colors.BLACK,
        content_padding=10,
        border=ft.InputBorder.NONE,
        bgcolor=ft.colors.BLUE_GREY,
        on_change=edita_view,
    )
    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(20),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,

            controls=[
                ft.Text(value='Para criar títulos em diferentes tamanhos', weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLACK),
                ft.Text(value='# H1', color=ft.colors.GREY_700),
                ft.Text(value='## H2', color=ft.colors.GREY_700),
                ft.Text(value='### H3', color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para formatar o estilo do texto', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Text(value='**Texto em negrito**', color=ft.colors.GREY_700),
                ft.Text(value='*Texto em itálico*', color=ft.colors.GREY_700),
                ft.Text(value='~~Texto tachado~~', color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para criar listas', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Text(value='1. Ordenada', color=ft.colors.GREY_700),
                ft.Text(value='- Desordenada', color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Inserir links e imagens', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Text(value='[Texto do link](https://programadoraventureiro.com)', color=ft.colors.GREY_700),
                ft.Text(value='![Label da imagem](image.jpg)', color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY, height=40),

                ft.Text(value='Para inserir código', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Text(value='`print("Código em uma linha")`', color=ft.colors.GREY_700),
                ft.Text(value='```\nprint("Código em mútiplas linhas") \n```', color=ft.colors.GREY_700),
            ]
        )
    )

    view= ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link=lambda e: page.launch_url(e.data),
    )

    layout = ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column([
                    editor,
                    how_to
                ])
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(20),
                content=view,
            ),
        ]
    )

    elementos = [
        layout,
    ]

    page.add(*elementos)


ft.app(target=main, assets_dir='assets')