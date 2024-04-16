import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    page.scroll=ft.ScrollMode.AUTO

    def handle_dismiss(e):
        lv.controls.remove(e.control)
        lv.update()
    
    elementos = [
        lv := ft.ListView(controls=[
            ft.Dismissible(
                content=ft.Text(value=f'Item {i}',size=40),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.AMBER, content=ft.Text('Arquivar',size=20)),
                secondary_background=ft.Container(bgcolor=ft.colors.RED, content=ft.Text('Excluir', size=20), alignment=ft.alignment.top_right),
                on_dismiss= handle_dismiss,
                on_update=lambda _: print('Atualizado'),
                on_resize=lambda _: print('Redimensionado'),
            ) for i in range(30)
        ])
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
