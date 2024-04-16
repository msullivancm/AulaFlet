import flet as ft

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    t = ft.Text('Shake Detector', size=30)
    def shake(e):
        t.value = 'Shake detected!'
        print('Shake detected!')

    shd = ft.ShakeDetector(
        minimum_shake_count=2,
        shake_slop_time_ms=200,
        shake_count_reset_time_ms=1000,
        on_shake=shake,
    )

    page.overlay.append(shd)
    page.add(t)
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
