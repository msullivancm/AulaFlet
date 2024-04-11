import flet as ft

def main(page:ft.Page):
    #page.bgcolor = '#b12b12'
    page.bgcolor = ft.colors.RED
    
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    
    page.padding = ft.padding.only(top=10, left=10, right=10, bottom=10)
    
    page.spacing = 100
    
    page.title = 'Hello World'
    
    page.add(
        ft.Text('Hello World!'), 
        ft.Container(ft.Text(value='Container'), bgcolor=ft.colors.BLUE),
        ft.Container(ft.Text(value='Container'), bgcolor=ft.colors.GREEN),
        )
    
    page.update()

ft.app(target=main)