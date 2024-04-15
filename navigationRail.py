import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0.0
    page.window_left = 1600.0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label='Inicio',
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CHAT,
                label='Chat',
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARKS,
                label='Itens salvos',
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor='red',height=20,width=20),
                selected_icon_content=ft.Container(bgcolor='green',width=20,height=20),
                label='Configurações',
                label_content=ft.Text('Configurações',size=20,weight=ft.FontWeight.BOLD),
                padding=ft.padding.all(10),
            ),
        ],
        bgcolor=ft.colors.GREEN_900,
        selected_index=0,
        extended=False,
        min_extended_width=200,
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    icon=ft.icons.SETTINGS,
                    text='Configurações',
                ),
                ft.PopupMenuItem(
                    icon=ft.icons.HELP,
                    text='Ajuda',
                ),
                ft.PopupMenuItem(
                    icon=ft.icons.EXIT_TO_APP,
                    text='Sair',
                ),
            ]
        ),
        leading=ft.CircleAvatar(content=ft.Text('PA')),
        on_change=lambda index: print('Index changed to', index.control.selected_index),
    )

    row = ft.Row(
        [rail],
        expand=True
    )
    elementos = [
        row,
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
