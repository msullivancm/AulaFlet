import flet as ft


def main(page: ft.Page):
    page.window_width = 400.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def change_route(e):
        match e.control.selected_index:
            case 0:
                page.go('/')
            case 1:
                page.go('/loja')
            case 2:
                page.go('/app')

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                route='/',
                appbar=ft.AppBar(
                    title=ft.Text('Home'),
                    bgcolor=ft.colors.BLUE,
                ),
                controls=[
                    ft.ElevatedButton(
                        text='Ir para loja',
                        on_click=lambda _: page.go('/loja')
                    ),
                    ft.ListView([
                        ft.Text(f'Item {i}', size=30) for i in range(50)
                    ])
                ],
                scroll=ft.ScrollMode.AUTO,
                auto_scroll=False,
                bgcolor=ft.colors.BLACK,

                drawer=ft.NavigationDrawer(controls=[
                    ft.NavigationDrawerDestination(label='Home', icon=ft.icons.HOME),
                    ft.NavigationDrawerDestination(label='Loja', icon=ft.icons.STORE),
                    ft.NavigationDrawerDestination(label='App', icon=ft.icons.PHONE_IPHONE),
                ],
                    on_change=change_route),
                end_drawer=ft.NavigationDrawer(controls=[
                    ft.NavigationDrawerDestination(label='Perfil', icon=ft.icons.PERSON),
                    ft.NavigationDrawerDestination(label='Configurações', icon=ft.icons.SETTINGS),
                    ft.NavigationDrawerDestination(label='Sair', icon=ft.icons.EXIT_TO_APP),
                ],
                    on_change=change_route),

                floating_action_button=ft.FloatingActionButton(
                    icon=ft.icons.PHONE_IPHONE,
                    on_click=lambda _: page.go('/app')
                ),
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                padding=ft.padding.all(20),
            )
        )
        if page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/loja',
                    appbar=ft.AppBar(
                        title=ft.Text('Loja'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text='Ir para home',
                            on_click=lambda _: page.go('/')
                        ),
                        ft.ElevatedButton(
                            text='Ir para app',
                            on_click=lambda _: page.go('/app')
                        )
                    ],
                    fullscreen_dialog=True, #Muda a animação e disposição dos elementos
                )
            )

        if page.route == '/app':
            page.views.append(
                ft.View(
                    route='/app',
                    appbar=ft.AppBar(
                        title=ft.Text('App'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text='Ir para home',
                            on_click=lambda _: page.go('/')
                        )
                    ]
                )
            )
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
    # ft.app(target=main, assets_dir='assets', view=ft.AppView.WEB_BROWSER)
