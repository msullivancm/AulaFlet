import flet as ft

def main(page:ft.Page):

    def open_dialog(e):
        page.dialog = ad1
        ad1.open = True
        page.update()

    def close_dialog(e):
        ad1.open = False
        page.update()

    ad1 = ft.AlertDialog(
        content=ft.Text(value='Você tem certeza que deseja excluir este item?'),
        title=ft.Text(value='Excluir item'),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(10),
        modal=False, # True: bloqueia a interação com a tela de fundo
        shape=ft.RoundedRectangleBorder(radius=10),
        on_dismiss= lambda _: print('Dialog dismissed'),
        actions=[
            ft.TextButton(text='Cancelar', on_click=close_dialog),
            ft.ElevatedButton(text='Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN) )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.add(
        ft.ElevatedButton(
            text='Abrir diálogo',
            on_click=open_dialog
        )
    )

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
