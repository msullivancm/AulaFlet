import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    icone = ft.Ref[ft.Icon]()
    titulo = ft.Ref[ft.Text]()
    subtitulo = ft.Ref[ft.Text]()

    layout = ft.Container(
        bgcolor=ft.colors.AMBER,
        padding=ft.padding.all(20),
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.RED,
                    padding=ft.padding.all(20),
                    content=ft.Icon(ref=icone, name=ft.icons.ABC),
                ),
                ft.Container(
                    bgcolor=ft.colors.BLUE,
                    padding=ft.padding.all(20),
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Text(ref=titulo, value='Titulo',size=30),
                            ft.Text(ref=subtitulo, value='Subtitulo'),
                        ]
                    )
                ),
            ]
        )
    )
    
    elementos = [
        layout,
    ]
    
    page.add(*elementos)

    icone.current.name = ft.icons.STORE
    icone.current.update()
    titulo.current.value = 'Titulo atualizado'
    titulo.current.update()
    subtitulo.current.value = 'Subtitulo atualizado'
    subtitulo.current.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
