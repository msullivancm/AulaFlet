import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    dg1 = ft.Row(
        controls=[
            ft.Draggable(
                group='color',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.RED,
                    border_radius=10,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.with_opacity(0.5,ft.colors.AMBER),
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.AMBER_300,
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
            ),
            ft.Draggable(
                group='color',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.BLUE_ACCENT,
                    border_radius=10,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLUE),
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.BLUE_GREY,
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
            ),
            ft.Draggable(
                group='color1',
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.GREEN,
                    border_radius=10,
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREEN),
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.GREEN_700,
                    border_radius=10,
                    shape=ft.BoxShape.CIRCLE,
                ),
            )
        ]
    )

    def drag_will_accept(e):
        e.control.content.border = ft.border.all(5,ft.colors.BLACK45 if e.data == "true" else ft.colors.RED)
        e.control.update()

    def drag_accept(e):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    target = ft.DragTarget(
        group='color',
        content=ft.Container(
            width=400,
            height=400,
            bgcolor=ft.colors.BLUE,
            border_radius=10,
        ),
        on_will_accept=drag_will_accept,
        on_accept=drag_accept,
        on_leave=drag_leave,
    )

    elementos = [
        dg1,
        target,
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
