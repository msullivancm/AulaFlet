import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon='menu', icon_color=ft.colors.WHITE),
                ft.Container(expand=True), # This container will expand to fill the space between the two icons
                ft.IconButton(icon='search'),
                ft.IconButton(icon='more_vert'),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
    )

    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
