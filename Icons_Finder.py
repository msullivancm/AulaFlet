import flet as ft


def icon_container(icon):
    return ft.Container(
        padding=ft.padding.all(20),
        bgcolor=ft.colors.WHITE10,
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(name=icon, size=50),
                ft.Text(value=icon)
            ],
        )
    )

def main(page: ft.Page):
    def search(e):
        value = e.control.value.upper()

        icons_grid.controls = []
        for icon in dir(ft.icons):
            if value in icon:
                icons_grid.controls.append(icon_container(icon=icon))

        icons_grid.update()


    searchbar = ft.TextField(
        prefix_icon=ft.icons.SEARCH,
        hint_text='Digite algo para buscar...',
        on_submit=search
    )

    icons_grid = ft.GridView(
        expand=True,
        controls=[],
        max_extent=200,
        child_aspect_ratio=1.0
    )

    layout = ft.Column(
        expand=True,
        controls=[
            searchbar,
            icons_grid
        ]
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target = main, view = ft.AppView.FLET_APP)