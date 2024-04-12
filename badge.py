import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def incrementar_badge(e, badge):
        badge.text = str(int(badge.text) + 1)
        page.update()

    elementos = [
        bg1 := ft.Badge(
            content=ft.Icon(name=ft.icons.NOTIFICATIONS, size=100),
            text='0',
        ),
        btn1 := ft.ElevatedButton(text='Incrementar', on_click=lambda e: incrementar_badge(e, bg1)),
    ]
    
    page.add(*elementos)

ft.app(target=main, assets_dir='assets')