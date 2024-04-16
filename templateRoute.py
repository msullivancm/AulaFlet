import flet as ft

def main(page:ft.Page):
    def route_change(route):
        troute = ft.TemplateRoute(page.route)

        if troute.match('/loja/:produto'):
            page.add(
                ft.Text(f'Produto: {troute.produto}')
            )
        elif troute.match('/loja/:produto/pedido/:id'):
            page.add(
                ft.Text(f'Produto: {troute.produto}, pedido: {troute.id}')
            )

    page.on_route_change = route_change
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
