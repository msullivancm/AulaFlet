import flet as ft
from partials.sidebar import Sidebar
from partials.content import MainContent

# xs	<576px
# sm	≥576px
# md	≥768px
# lg	≥992px
# xl	≥1200px
# xxl	≥1400px

class AppTheme:
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background='#20202a',
            on_background='#2d2d3a',
            on_inverse_surface='#2d2d3a',
            primary=ft.colors.AMBER,
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                size=14,
            ),
            body_medium=ft.TextStyle(
                weight=ft.FontWeight.NORMAL,
                color=ft.colors.GREY,
                size=14,
            ),
            headline_large=ft.TextStyle(
                weight=ft.FontWeight.W_900,
                color=ft.colors.WHITE,
                size=50,
            ),
            label_large=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=16,
            ),
            headline_medium=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=30,
            )
        ),
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=False,
            track_color={
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            },
            thumb_color={
                ft.MaterialState.HOVERED: ft.colors.TRANSPARENT,
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            }
        )
    )


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme = AppTheme.theme
        self.page.on_resize = self.show_app_bar
        self.page.bgcolor = ft.colors.BLACK
        self.main()
        self.show_app_bar()

    def toggle_sidebar(self, e):
        self.sidebar.col['xs'] = 12 if self.sidebar.col['xs'] == 0 else 0
        self.content.col['xs'] = 0 if self.content.col['xs'] == 12 else 12
        self.page.update()


    def show_app_bar(self, e = None):
        if self.page.width < 768:
            self.page.appbar = ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color=ft.colors.WHITE,
                    on_click=self.toggle_sidebar
                ),
                bgcolor=ft.colors.BACKGROUND,
            )
            self.layout.spacing = 0
            self.page.bgcolor = ft.colors.BACKGROUND
        else:
            self.page.appbar = None
            self.layout.spacing = 10
            self.page.bgcolor = ft.colors.BLACK

        self.page.update()

    def main(self):
        self.sidebar = Sidebar(col={'xs': 0, 'md': 5, 'lg': 4, 'xxl': 3})
        self.content = MainContent(col={'xs': 12, 'md': 7, 'lg': 8, 'xxl': 9})

        self.layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content,
            ],
            expand=True,
        )

        self.page.add(self.layout)



if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')