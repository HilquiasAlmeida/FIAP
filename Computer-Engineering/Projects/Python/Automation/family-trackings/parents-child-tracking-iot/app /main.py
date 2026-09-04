import flet as ft

def main(page: ft.Page):
    page.title = "Family Trackings IoT - Painel Pais & Filhos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    def route_change(e):
        page.views.clear()
        
        # 1. Tela de Login (Página Inicial)
        if page.route == "/" or page.route == "/login":
            user_field = ft.TextField(label="E-mail ou Usuário", width=300, border_radius=8, prefix_icon=ft.Icons.EMAIL)
            pass_field = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300, border_radius=8, prefix_icon=ft.Icons.LOCK)
            error_text = ft.Text("", color=ft.Colors.RED)

            async def do_login(e):
                if not user_field.value or not pass_field.value:
                    error_text.value = "Por favor, preencha o e-mail e a senha!"
                    page.update()
                else:
                    await page.push_route("/dashboard")

            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Icon(ft.Icons.SECURITY, size=64, color=ft.Colors.INDIGO),
                                    ft.Text("Family Trackings IoT", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                                    ft.Text("Faça login para monitorar seus dependentes", size=14, color=ft.Colors.GREY_700),
                                    ft.Container(height=10),
                                    user_field,
                                    pass_field,
                                    ft.ElevatedButton(
                                        content=ft.Row([ft.Icon(ft.Icons.LOGIN, color=ft.Colors.WHITE), ft.Text("Entrar", color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
                                        bgcolor=ft.Colors.INDIGO,
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
                    bgcolor=ft.Colors.GREY_50
                )
            )

        # 2. Tela Principal / Dashboard
        elif page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.AppBar(
                            title=ft.Text("Family Trackings - Monitoramento", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.INDIGO,
                            center_title=True,
                            actions=[
                                ft.IconButton(ft.Icons.LOGOUT, tooltip="Sair", icon_color=ft.Colors.WHITE, on_click=lambda _: page.run_task(page.push_route, "/login"))
                            ]
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Dispositivos Conectados", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.Icons.PHONE_ANDROID, color=ft.Colors.INDIGO),
                                                    title=ft.Text("Smartphone - Filho (João)", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Status: Online • Localização: Escola • Bateria: 85%"),
                                                ),
                                                ft.Row([
                                                    ft.TextButton(content=ft.Text("Ver no Mapa"), on_click=lambda _: page.run_task(page.push_route, "/tracking")),
                                                ], alignment=ft.MainAxisAlignment.END)
                                            ]),
                                            padding=10
                                        )
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.Icons.WATCH, color=ft.Colors.INDIGO),
                                                    title=ft.Text("Smartwatch - Filha (Maria)", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Status: Online • Localização: Parque • Bateria: 62%"),
                                                ),
                                                ft.Row([
                                                    ft.TextButton(content=ft.Text("Ver no Mapa"), on_click=lambda _: page.run_task(page.push_route, "/tracking")),
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
                        content=ft.Row([ft.Icon(ft.Icons.ADD, color=ft.Colors.WHITE), ft.Text("Vincular Novo Dispositivo", color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
                        bgcolor=ft.Colors.INDIGO,
                        on_click=lambda _: page.run_task(page.push_route, "/add-device")
                    ),
                )
            )

        # 3. Tela de Adicionar Dispositivo
        elif page.route == "/add-device":
            device_code = ft.TextField(label="Código do Dispositivo (IMEI / UUID)", border_radius=8)
            device_name = ft.TextField(label="Nome do Dependente / Aparelho", border_radius=8)
            status_text = ft.Text("", color=ft.Colors.GREEN)

            def save_device(e):
                if not device_code.value or not device_name.value:
                    status_text.value = "Por favor, preencha todos os campos!"
                    status_text.color = ft.Colors.RED
                else:
                    status_text.value = "Dispositivo vinculado com sucesso!"
                    status_text.color = ft.Colors.GREEN
                page.update()

            page.views.append(
                ft.View(
                    "/add-device",
                    [
                        ft.AppBar(
                            title=ft.Text("Vincular Novo Dispositivo", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.run_task(page.push_route, "/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Cadastre um novo rastreador IoT", size=18, weight=ft.FontWeight.BOLD),
                                    device_name,
                                    device_code,
                                    ft.ElevatedButton(
                                        content=ft.Row([ft.Icon(ft.Icons.CHECK, color=ft.Colors.WHITE), ft.Text("Salvar e Vincular", color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
                                        bgcolor=ft.Colors.INDIGO,
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
                            title=ft.Text("Rastreamento em Tempo Real", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.run_task(page.push_route, "/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Localização Atual dos Dependentes", size=18, weight=ft.FontWeight.BOLD),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED),
                                                    title=ft.Text("João - Escola Estadual", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Última atualização: há 2 minutos\nCoordenadas: -23.5505, -46.6333"),
                                                ),
                                            ]),
                                            padding=10
                                        )
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.GREEN),
                                                    title=ft.Text("Maria - Parque Ibirapuera", weight=ft.FontWeight.BOLD),
                                                    subtitle=ft.Text("Última atualização: há 5 minutos\nCoordenadas: -23.5882, -46.6582"),
                                                ),
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

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None)

if __name__ == "__main__":
    ft.run(main)
