import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0.0
    page.window_left = 1600.0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label='Item 1',
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.NavigationDrawerDestination(
                label='Item 2',
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            )
        ]
    )

    def show_drawer():
        page.drawer.open = True
        page.update()

    def hide_drawer():
        page.drawer.open = False
        page.update()

    page.drawer.open = True
    page.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
