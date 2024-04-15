import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def close_banner(e):
        page.banner.open = False
        page.update()

    def open_banner(e):
        page.banner = bn1
        bn1.open = True
        page.update()

    bn1 = ft.Banner(
        content=ft.Text('Não foi possível executar a operação.'),
        content_padding=ft.padding.all(30),
        leading=ft.Icon(ft.icons.ERROR, color=ft.colors.RED),
        force_actions_below=True,
        bgcolor=ft.colors.AMBER_100,
        actions=[
            ft.TextButton('Tentar novamente', style=ft.ButtonStyle(color=ft.colors.RED) ),
            ft.ElevatedButton('Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner)
        ]
    )

    btn1 = ft.ElevatedButton('Abrir banner', on_click=open_banner)

    elementos = [
        btn1,
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
