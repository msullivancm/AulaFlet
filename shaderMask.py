import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50
    
    elementos = [
        sm := ft.ShaderMask(
            content=ft.Text(value='TESTE', size=100),
            shader=ft.LinearGradient(colors=[ft.colors.DEEP_PURPLE,ft.colors.CYAN])
        )
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
