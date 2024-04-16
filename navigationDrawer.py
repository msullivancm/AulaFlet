import flet as ft

def main(page:ft.Page):
    page.window_width = 800.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0
    
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
            ),
            ft.NavigationDrawerDestination(
                label='Item 3',
                icon=ft.icons.PHONE_OUTLINED,
                selected_icon=ft.icons.PHONE,
            )
        ],
        bgcolor=ft.colors.GREY_900,
        indicator_color=ft.colors.DEEP_ORANGE,
        indicator_shape=ft.RoundedRectangleBorder(radius=10),
        selected_index=1,
        tile_padding=ft.padding.all(20),

        on_change=lambda index: print(f'Item {index.control.selected_index} selected'),
    )

    def show_drawer(e):
        page.drawer.open = not page.drawer.open
        page.drawer.update()

    btn = ft.IconButton(
        icon=ft.icons.MENU,
        on_click=show_drawer,
    )
    page.add(btn)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
