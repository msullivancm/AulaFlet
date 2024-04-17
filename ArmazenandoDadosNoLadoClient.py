import flet as ft


def main(page: ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 50
    page.padding = 20
    page.padding = ft.padding.all(50)

    def atualizar_lista():
        items = page.client_storage.get('tasks')

        if not items:
            items = []

        def change_status(e):
            item = {'label': e.control.label, 'selected': e.control.value}
            print(item)
            print(e.control.data)
            items[e.control.data]=item
            page.client_storage.set('tasks', items)

        lv.controls = [
            ft.Checkbox(
                value=item.get('selected'),
                label=item.get('label'),
                adaptive=True,
                on_change=change_status,
                data=index
            ) for index, item in enumerate(items)
        ]

        lv.update()

    def adicionar_tarefa(e):
        item = {'label': e.control.value, 'selected': False}
        items = page.client_storage.get('tasks')

        if not items:
            items = []

        items.append(item)

        page.client_storage.set('tasks', items)
        e.control.value = ''
        e.control.update()
        atualizar_lista()

    tarefa = ft.TextField(label='Tarefa', on_submit=adicionar_tarefa)
    lv = ft.ListView()

    page.add(tarefa, lv)
    atualizar_lista()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
