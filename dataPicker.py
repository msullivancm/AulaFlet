import datetime

import flet as ft

def main(page:ft.Page):
    page.window_width = 365.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 2199.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    dp = ft.DatePicker(
        cancel_text='Cancelar',
        confirm_text='Confirmar',
        error_format_text='Formato inválido',
        field_hint_text='MM/DD/YYYY',
        field_label_text='Digite uma data',
        help_text='Selecione uma data',
        switch_to_calendar_icon=ft.icons.CALENDAR_MONTH,
        switch_to_input_icon=ft.icons.EDIT,

        # date_picker_mode = ft.DatePickerMode.YEAR,
        date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR,
        value=datetime.date(2024,1,28),
        first_date=datetime.date(2024,1,1),
        last_date=datetime.date(2024,12,31),
        error_invalid_text='Data fora do limite',

        on_change=lambda _: print(dp.value),
        on_dismiss=lambda _: print('Saiu'),

        keyboard_type=ft.KeyboardType.NUMBER
    )

    page.overlay.append(dp)

    elementos = [
        btn := ft.ElevatedButton('Abrir', on_click=lambda _: dp.pick_date())
    ]

    page.add(*elementos)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
