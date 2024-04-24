import flet as ft
from components.skills import SkillRing, SkillProgressBar

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    ),
                    ft.Text(value='Marcus Sullivan', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Fullstack', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center,
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Rio de Janeiro', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='45', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        languages = ft.Row(
            controls=[
                SkillRing(title='Português', value=1),
                SkillRing(title='Inglês', value=0.8),
                SkillRing(title='Espanhol', value=0.5),
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressBar(title='PYTHON', value=1),
                SkillProgressBar(title='FLUTTER', value=0.6),
                SkillProgressBar(title='JAVA SCRIPT', value=0.5),
                SkillProgressBar(title='JAVA', value=0.6),
                SkillProgressBar(title='ADVPL/PROTHEUS', value=1),
                SkillProgressBar(title='BANCO DE DADOS', value=1),
                SkillProgressBar(title='SISTEMAS OPERACIONAIS', value=1),
                SkillProgressBar(title='DEVOPS', value=0.8),
            ]
        )

        technologies = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value='Scripting, bash, sh, Python, Windows bach script and PowerShell', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Languages - Python, ADVPL (ERP Protheus), Java, C#, Flutter, PHP, Java Script and also HTML and CSS', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Database - MSSQL, Oracle, Mysql, and Postgresql', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='DevOps - Git, Docker, Docker-Compose, Swarm, Vagrant, and Kubernetes', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Virtualization - VirtualBox, Hyper-V, VMWare, and Xen', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Operational Systems - Linux, Windows, MAC OS, HP-UX and Solaris', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Monitoring - Zabbix, Cacti and Nagios', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Cloud Computing - Google Cloud, Amazon Cloud, Microsoft Azure, and OpenStack', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='ERP TOTVS Protheus, TOTVS RM and Sankhya', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='ECM - TOTVS Fluig, Alfresco and M-Files', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Agile Development, Agile Infrastructure, ITIL, PMBOK-based Project Management', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )


        cv = ft.TextButton(
            text='DOWNLOAD CV',
            style=ft.ButtonStyle(color=ft.colors.GREY),
            icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.GREY,
            url='https://drive.google.com/file/d/1JhVP355VhBD_MqIiV6topQFU1Cr67QsI/view?usp=sharing',

            # https://sites.google.com/site/gdocs2direct/?pli=1
        )


        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    ft.Divider(height=30),
                    cv,
                ]
            )
        )


class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding = ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png', height=15, color='white'),
                        url='https://www.instagram.com/msullivancm/',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color='white'),
                        url='https://www.linkedin.com/in/msullivancm',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color='white'),
                        url='https://github.com/msullivancm',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png', height=15, color='white'),
                        url='https://www.youtube.com/channel/UCEfRP-wXeAu68i1aY5fLfRA',
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        )