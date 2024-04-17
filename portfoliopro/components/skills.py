import flet as ft 

class Skill(ft.UserControl):
    def __init__(self, title: str, value: float):
        super().__init__()
        self.title = title
        self.value = value


class SkillRing(Skill):
    def build(self):
        self.expand = True

        return ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        ft.PieChart(
                            sections=[
                                ft.PieChartSection(value=self.value, color=ft.colors.PRIMARY, radius=5),
                                ft.PieChartSection(value=1 - self.value, color=ft.colors.BLACK26, radius=5),
                            ],
                            sections_space=0,
                            center_space_color=ft.colors.BLACK12,
                            height=70,
                        ),
                        ft.Container(
                            content=ft.Text(value=f'{self.value:.0%}', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            alignment=ft.alignment.center,
                            height=70,
                        )
                    ]
                ),
                ft.Text(value=self.title, theme_style=ft.TextThemeStyle.BODY_LARGE),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # expand=True,
        )

class SkillProgressBar(Skill):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(value=self.title, theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value=f'{self.value:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.ProgressBar(value=self.value, color=ft.colors.PRIMARY, bgcolor=ft.colors.BLACK26),
                    ft.Divider(height=10, color=ft.colors.BLACK12),
                ]
            )
        )