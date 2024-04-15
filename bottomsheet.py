import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def show_bottom_sheet(e):
        bs.open = True
        page.update()

    def hide_botton_sheet(e):
        bs.open = False
        page.update()

    bs = ft.BottomSheet(
        content = ft.Container(
            ft.Column(
                controls=[
                    ft.Text('Título', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text('Conteúdo do bottomsheet', style=ft.TextThemeStyle.BODY_LARGE),
                    ft.FilledButton('Fechar', on_click=hide_botton_sheet)
                ],
            ),
            padding = 20,
        ),
        dismissible=False,
        enable_drag=True,
        is_scroll_controlled=True,
        maintain_bottom_view_insets_padding=True,
        show_drag_handle=True,
    )
    
    page.overlay.append(bs)

    btn = ft.FilledButton('Mostrar BottomSheet', on_click=show_bottom_sheet)

    page.add(btn)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
