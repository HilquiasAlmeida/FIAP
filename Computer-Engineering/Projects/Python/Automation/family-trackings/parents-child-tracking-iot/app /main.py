import flet as ft

def main(page: ft.Page):
    page.title = "Family Trackings IoT - Painel Pais & Filhos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    def route_change(e):
        page.views.clear()
        
        # 1. Tela de Login
        if page.route == "/" or page.route == "/login":
            user_field = ft.TextField(label="E-mail ou Usuário", width=300, border_radius=8, prefix_icon=ft.icons.EMAIL)
            pass_field = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300, border_radius=8, prefix_icon=ft.icons.LOCK)
            error_text = ft.Text("", color=ft.colors.RED)

            def do_login(e):
                if not user_field.value or not pass_field.value:
                    error_text.value = "Por favor, preencha o e-mail e a senha!"
                    page.update()
                else:
                    page.go("/dashboard")

            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Icon(ft.icons.SECURITY, size=64, color=ft.colors.INDIGO),
                                    ft.Text("Family Trackings IoT", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.INDIGO_900),
                                    ft.Text("Faça login para monitorar seus dependentes", size=14, color=ft.colors.GREY_700),
                                    ft.Container(height=10),
                                    user_field,
                                    pass_field,
                                    ft.ElevatedButton(
                                        content=ft.Row(
                                            [ft.Icon(ft.icons.LOGIN), ft.Text("Entrar")],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=5
                                        ),
                                        bgcolor=ft.colors.INDIGO,
                                        color=ft.colors.WHITE,
                                        width=300,
                                        on_click=do_login
                                    ),
                                    error_text,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=15,
                            ),
                            alignment=ft.alignment.center,
                            expand=True,
                            padding=20
                        )
                    ],
                    bgcolor=ft.colors.GREY_50
                )
            )

        # 2. Tela Principal / Dashboard
        elif page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.AppBar(
                            title=ft.Text("Family Trackings - Monitoramento", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                            bgcolor=ft.colors.INDIGO,
                            center_title=True,
                            actions=[
                                ft.IconButton(ft.icons.LOGOUT, tooltip="Sair", icon_color=ft.colors.WHITE, on_click=lambda _: page.go("/login"))
                            ]
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Dispositivos Conectados", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.INDIGO_900),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.icons.PHONE_ANDROID, color=ft.colors.INDIGO),
                                                    title=ft.Text("Smartphone - Filho (João)", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Status: Online • Localização: Escola • Bateria: 85%"),
                                                ),
                                                ft.Row([
                                                    ft.ElevatedButton(
                                                        text="Ver no Mapa",
                                                        on_click=lambda _: page.go("/tracking")
                                                    ),
                                                ], alignment=ft.MainAxisAlignment.END)
                                            ]),
                                            padding=10
                                        )
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.icons.WATCH, color=ft.colors.INDIGO),
                                                    title=ft.Text("Smartwatch - Filha (Maria)", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Status: Online • Localização: Parque • Bateria: 62%"),
                                                ),
                                                ft.Row([
                                                    ft.ElevatedButton(
                                                        text="Ver no Mapa",
                                                        on_click=lambda _: page.go("/tracking")
                                                    ),
                                                ], alignment=ft.MainAxisAlignment.END)
                                            ]),
                                            padding=10
                                        )
                                    ),
                                ],
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                            ),
                            padding=20,
                            expand=True,
                        )
                    ],
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Row([ft.Icon(ft.icons.ADD), ft.Text("Vincular Novo Dispositivo")], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                        bgcolor=ft.colors.INDIGO,
                        color=ft.colors.WHITE,
                        on_click=lambda _: page.go("/add-device")
                    ),
                )
            )

        # 3. Tela de Adicionar Dispositivo
        elif page.route == "/add-device":
            device_code = ft.TextField(label="Código do Dispositivo (IMEI / UUID)", border_radius=8)
            device_name = ft.TextField(label="Nome do Dependente / Aparelho", border_radius=8)
            status_text = ft.Text("", color=ft.colors.GREEN)

            def save_device(e):
                if not device_code.value or not device_name.value:
                    status_text.value = "Por favor, preencha todos os campos!"
                    status_text.color = ft.colors.RED
                else:
                    status_text.value = "Dispositivo vinculado com sucesso!"
                    status_text.color = ft.colors.GREEN
                page.update()

            page.views.append(
                ft.View(
                    "/add-device",
                    [
                        ft.AppBar(
                            title=ft.Text("Vincular Novo Dispositivo", color=ft.colors.WHITE),
                            bgcolor=ft.colors.INDIGO,
                            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Cadastre um novo rastreador IoT", size=18, weight=ft.FontWeight.BOLD),
                                    device_name,
                                    device_code,
                                    ft.ElevatedButton(
                                        content=ft.Row(
                                            [ft.Icon(ft.icons.CHECK), ft.Text("Salvar e Vincular")],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=5
                                        ),
                                        bgcolor=ft.colors.INDIGO,
                                        color=ft.colors.WHITE,
                                        on_click=save_device,
                                        width=250
                                    ),
                                    status_text,
                                ],
                                spacing=20,
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            padding=20,
                            expand=True,
                        )
                    ]
                )
            )

        # 4. Tela de Rastreamento
        elif page.route == "/tracking":
            page.views.append(
                ft.View(
                    "/tracking",
                    [
                        ft.AppBar(
                            title=ft.Text("Rastreamento em Tempo Real", color=ft.colors.WHITE),
                            bgcolor=ft.colors.INDIGO,
                            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Localização Atual dos Dependentes", size=18, weight=ft.FontWeight.BOLD),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.RED),
                                                    title=ft.Text("João - Escola Estadual", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Última atualização: há 2 minutos\nCoordenadas: -23.5505, -46.6333"),
                                                )
                                            ]),
                                            padding=10
                                        )
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.GREEN),
                                                    title=ft.Text("Maria - Parque Ibirapuera", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Última atualização: há 5 minutos\nCoordenadas: -23.5882, -46.6582"),
                                                )
                                            ]),
                                            padding=10
                                        )
                                    ),
                                ],
                                spacing=15,
                            ),
                            padding=20,
                            expand=True,
                        )
                    ]
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
