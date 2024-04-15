import flet as ft

def main(page:ft.Page):
    page.snack_bar = ft.SnackBar(
        content=ft.Text('Não foi possível processar.'),
        bgcolor=ft.colors.RED_100,
        show_close_icon=True,
        close_icon_color=ft.colors.RED,
        padding=ft.padding.all(10),
        duration=10000, #duação em milissegundos
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.margin.all(50),
        dismiss_direction=ft.DismissDirection.HORIZONTAL,
        action='Confirmar',
        action_color=ft.colors.BLUE,
        on_action=lambda _: print('clicado')
    )

    def show_snackbar(e):
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.ElevatedButton('Abre Snackbar', on_click=show_snackbar)
    )

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
