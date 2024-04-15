import flet as ft

def main(page:ft.Page):
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0.0
    page.window_left = 1600.0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    page.appbar = ft.AppBar(
        title=ft.Text('Título'),
        bgcolor=ft.colors.BLUE,
        center_title=False,
        toolbar_height=50,
        color=ft.colors.AMBER,
        leading=ft.Icon(ft.icons.HOME),
        #leading=ft.Image(src='assets/icons/icon-192.png'),
        leading_width=30,
        actions=[
            ft.IconButton(icon=ft.icons.SUNNY, on_click=lambda _: print('ligth mode')),
            ft.CircleAvatar(content=ft.Text(value='MS'), color=ft.colors.AMBER),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Meus dados'),
                    ft.PopupMenuItem(text='Configurações'),
                    ft.PopupMenuItem(), #separador
                    ft.PopupMenuItem(text='Sair'),
                ]
            )
        ]
    )

    elementos = [
        
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
