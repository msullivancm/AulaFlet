import flet as ft


def main(page: ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    # Page resized 300.0 1039.0 0.0 1627.0

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    audio = ft.Audio(
        src='https://luan.xyz/files/audio/ambient_c_motion.mp3',
        autoplay=False,
        balance=0,
        volume=0.3,
        on_loaded=lambda _: print('Audio loaded'),
        on_duration_changed=lambda _: print('Audio duration changed', _.data),
        on_position_changed=lambda _: print('Audio position changed', _.data),
        on_state_changed=lambda _: print('Audio state changed', _.data),
        on_seek_complete=lambda _: print('Audio seek complete', _.data),
    )

    page.overlay.append(audio)

    t = ft.Text('Volume' + str(audio.volume))

    def volume_down(e):
        audio.volume -= 0.1
        t.value = 'Volume' + str(audio.volume)
        page.update()

    def volume_up(e):
        audio.volume += 0.1
        t.value = 'Volume' + str(audio.volume)
        page.update()

    def balance_left(e):
        audio.balance -= 0.1
        page.update()

    def balance_rigth(e):
        audio.balance += 0.1
        page.update()

    elementos = [
        t,
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.PLAY_CIRCLE, on_click=lambda _: audio.play()),
                ft.IconButton(icon=ft.icons.PAUSE_CIRCLE, on_click=lambda _: audio.pause()),
                ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda _: audio.resume()),
                ft.IconButton(icon=ft.icons.REPLAY_10,
                              on_click=lambda _: audio.seek(audio.get_current_position() - 10)),
                ft.IconButton(icon=ft.icons.FORWARD_10,
                              on_click=lambda _: audio.seek(audio.get_current_position() + 10)),

            ]
        ),
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.VOLUME_UP, on_click=volume_up),
                ft.IconButton(icon=ft.icons.VOLUME_DOWN, on_click=volume_down),
                ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=balance_left),
                ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=balance_rigth),
            ]
        )
    ]

    page.add(*elementos)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
