import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0.0
    page.window_left = 1600.0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME,
                label='Início',
            ),
            ft.NavigationDestination(
                icon=ft.icons.CHAT,
                label='Chat',
            ),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Itens Salvos',
            ),
            ft.NavigationDestination(
                icon_content=ft.Container(bgcolor=ft.colors.RED, width=30, height=30),
                selected_icon_content=ft.Container(bgcolor=ft.colors.GREEN, width=30, height=30),
                label='Perfil',
                tooltip='Perfil do usuário',
            ),
        ],
        selected_index=1,
        indicator_color=ft.colors.PINK,
        indicator_shape=ft.RoundedRectangleBorder(radius=20),
        on_change=lambda e: print('Selecionado:', e.control.selected_index),
    )

    elementos = [

    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
