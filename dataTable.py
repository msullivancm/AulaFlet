import flet as ft


def main(page: ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f'Selecionado a linha de índice {e.control.data}')
        e.control.update()

    dt = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nome")),
            ft.DataColumn(label=ft.Text('Login'), tooltip='login do usuário na plataforma'),
            ft.DataColumn(label=ft.Text('Idade'), numeric=True,
                          on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('Maria'),
                                show_edit_icon=True,
                                on_tap=lambda _: print('Célula clicada')),
                    ft.DataCell(content=ft.Text('mary99')),
                    ft.DataCell(content=ft.Text('43')),
                ],
                selected=True,
                on_select_changed=toggle_select,
                data=0,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('José'),
                                show_edit_icon=True,
                                on_tap=lambda _: print('Célula clicada')),
                    ft.DataCell(content=ft.Text('jose99')),
                    ft.DataCell(content=ft.Text('42')),
                ],
                selected=False,
                on_select_changed=toggle_select,
                data=1,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text('Luiz'),
                                show_edit_icon=True,
                                on_tap=lambda _: print('Célula clicada')),
                    ft.DataCell(content=ft.Text('luiz20')),
                    ft.DataCell(content=ft.Text('45')),
                ],
                selected=False,
                on_select_changed=toggle_select,
                data=2,
            )
        ],
        show_checkbox_column=True,
        bgcolor=ft.colors.GREY_900,
        border=ft.border.all(width=2,color=ft.colors.BLACK),
        border_radius=ft.border_radius.all(10),
        column_spacing=100,
        data_row_max_height=30,
        data_row_min_height=10,
        data_text_style=ft.TextStyle(italic=True),
        divider_thickness=3,
        gradient=ft.LinearGradient(begin=ft.alignment.top_left,end=ft.alignment.bottom_right,colors=[ft.colors.TEAL,ft.colors.CYAN]),
        data_row_color={
            ft.MaterialState.SELECTED:ft.colors.RED,
            ft.MaterialState.DEFAULT:ft.colors.GREY_700,
        },
        heading_row_color=ft.colors.BLACK,
        heading_row_height=50,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        horizontal_lines=ft.BorderSide(width=3,color=ft.colors.AMBER),
        vertical_lines=ft.BorderSide(width=3,color=ft.colors.AMBER),
        horizontal_margin=50,
        show_bottom_border=True,
        sort_column_index=2, #ordena por idade
        sort_ascending=True,
    )

    elementos = [
        dt,
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
