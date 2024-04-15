import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0.0
    page.window_left = 1600.0
    # Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    t = ft.Tabs(
        tabs=[
            ft.Tab(
                text='Tab 1',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 1'),
                )
            ),
            ft.Tab(
                icon=ft.icons.SETTINGS,
                text='Tab 2',
                content=ft.Text('Conteúdo da TAB 2')

            ),
            ft.Tab(
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 3'),
                ),
                tab_content=ft.Container(
                    bgcolor=ft.colors.GREEN,
                    content=ft.CircleAvatar(
                        foreground_image_url='assets/icons/icon-192.png',
                        tooltip='TESTE'
                    ),
                )
            ),
            ft.Tab(
                text='Tab 4',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 4'),
                )
            ),
            ft.Tab(
                text='Tab 5',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 5'),
                )
            ),
            ft.Tab(
                text='Tab 6',
                content=ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text('Conteúdo da TAB 6'),
                )
            )
        ],
        animation_duration=500,
        selected_index=1, #Seleciona a segunda tab
        divider_color=ft.colors.AMBER,
        indicator_color=ft.colors.AMBER_500,
        indicator_border_radius=ft.border_radius.all(10),
        indicator_padding=ft.padding.all(5),
        indicator_tab_size=True,
        label_color=ft.colors.GREEN,
        unselected_label_color=ft.colors.BLUE,
        overlay_color={
            ft.MaterialState.DEFAULT: ft.colors.RED,
            ft.MaterialState.HOVERED: ft.colors.PINK
        },
        scrollable=True, # melhor opção
    )

    elementos = [
        t,
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
