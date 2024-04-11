import flet as ft

def main(page:ft.Page):
    #page.bgcolor = '#b12b12'
    page.bgcolor = ft.colors.RED
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.padding = ft.padding.only(top=10, left=10, right=10, bottom=10)
    page.spacing = 100
    page.title = 'Aula 2 - Flet'
    page.window_always_on_top = True
    #Cria um app flutuante
    page.window_title_bar_hidden = False
    page.window_frameless = False
    #page.window_full_screen = True
    page.window_width = 300.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 1627.0
    
    #Exibe barra de progresso no icone do flet
    page.window_progress_bar = 0.5
    
    print(page.platform)
    
    def page_resize(e):
        print('Page resized', page.window_width, page.window_height, page.window_top, page.window_left)
    page.on_resize = page_resize
    
    def window_event(e):
        match e.data:
            case 'moved':
                print('Window moved', page.window_top, page.window_left)
            case 'resized':
                print('Window resized', page.window_width, page.window_height)
            case 'minimize':
                print('Window minimized')
            case _:
                print('Window event', e.data)
    page.on_window_event = window_event
    
    page.add(
        ft.Text('Hello World!'), 
        ft.Container(ft.Text(value='Container'), bgcolor=ft.colors.BLUE),
        ft.Container(ft.Text(value='Container'), bgcolor=ft.colors.GREEN),
        )
    
    page.update()

ft.app(target=main)