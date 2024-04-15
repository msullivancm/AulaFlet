import datetime

import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    tp = ft.TimePicker(
        cancel_text='Cancelar',
        confirm_text='Confirmar',
        error_invalid_text='Hora inválida',
        hour_label_text='Hora',
        minute_label_text='Minutos',
        help_text='Selecione a hora',
        time_picker_entry_mode=ft.TimePickerEntryMode.DIAL,

        value=datetime.time(22,31,18),
        on_change=lambda _: print(tp.value)
    )

    page.overlay.append(tp)

    def show_timepicker(e):
        tp.open = True
        page.update()

    elementos = [
        btn := ft.ElevatedButton('Abrir', on_click=lambda _: tp.pick_time())
    ]
    
    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
