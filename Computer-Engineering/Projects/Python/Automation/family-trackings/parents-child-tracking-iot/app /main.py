import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Family Trackings IoT - Painel Pais & Filhos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # Banco de dados simulado em memória (Sessão)
    if not hasattr(page, "devices"):
        page.devices = [
            {"id": "IMEI-001", "name": "Smartphone - João", "type": "Celular", "status": "Online", "battery": "85%"},
            {"id": "IMEI-002", "name": "Smartwatch - Maria", "type": "Relógio", "status": "Online", "battery": "62%"}
        ]
    
    if not hasattr(page, "access_log"):
        page.access_log = [
            {"user": "Pai (Admin)", "action": "Login realizado no sistema", "time": datetime.now().strftime("%d/%m/%Y %H:%M")},
        ]

    if not hasattr(page, "location_history"):
        page.location_history = [
            {"child": "João", "location": "Escola Estadual", "time": "Há 2 minutos", "coords": "-23.5505, -46.6333"},
            {"child": "Maria", "location": "Parque Ibirapuera", "time": "Há 10 minutos", "coords": "-23.5882, -46.6582"},
            {"child": "João", "location": "Residência", "time": "Há 1 hora", "coords": "-23.5500, -46.6300"}
        ]

    def route_change(e):
        page.views.clear()
        
        # 1. Tela de Login
        if page.route == "/" or page.route == "/login":
            user_field = ft.TextField(label="E-mail ou Usuário", width=300, border_radius=8, prefix_icon=ft.Icons.EMAIL)
            pass_field = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300, border_radius=8, prefix_icon=ft.Icons.LOCK)
            error_text = ft.Text("", color=ft.Colors.RED)

            def do_login(e):
                if not user_field.value or not pass_field.value:
                    error_text.value = "Por favor, preencha o e-mail e a senha!"
                    page.update()
                else:
                    page.access_log.insert(0, {"user": user_field.value, "action": "Login realizado com sucesso", "time": datetime.now().strftime("%d/%m/%Y %H:%M")})
                    page.go("/dashboard")

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
                                        text="Entrar",
                                        icon=ft.Icons.LOGIN,
                                        bgcolor=ft.Colors.INDIGO,
                                        color=ft.Colors.WHITE,
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
            device_list_col = ft.Column(spacing=10)

            def refresh_devices():
                device_list_col.controls.clear()
                for dev in page.devices:
                    device_list_col.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.PHONE_ANDROID if dev['type'] == 'Celular' else ft.Icons.WATCH, color=ft.Colors.INDIGO),
                                        title=ft.Text(dev["name"], weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text(f"ID: {dev['id']} • Status: {dev['status']} • Bateria: {dev['battery']}"),
                                    ),
                                    ft.Row([
                                        ft.TextButton("Editar", icon=ft.Icons.EDIT, on_click=lambda e, d=dev: page.go(f"/edit-device?id={d['id']}")),
                                        ft.TextButton("Excluir", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=lambda e, d=dev: delete_dev(d['id'])),
                                        ft.ElevatedButton("Ver no Mapa", icon=ft.Icons.MAP, on_click=lambda _: page.go("/tracking")),
                                    ], alignment=ft.MainAxisAlignment.END)
                                ]),
                                padding=10
                            )
                        )
                    )
                page.update()

            def delete_dev(dev_id):
                page.devices = [d for d in page.devices if d["id"] != dev_id]
                page.access_log.insert(0, {"user": "Administrador", "action": f"Removeu dispositivo {dev_id}", "time": datetime.now().strftime("%d/%m/%Y %H:%M")})
                refresh_devices()

            refresh_devices()

            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.AppBar(
                            title=ft.Text("Family Trackings - Monitoramento IoT", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.INDIGO,
                            center_title=True,
                            actions=[
                                ft.IconButton(ft.Icons.HISTORY, tooltip="Histórico de Acessos", icon_color=ft.Colors.WHITE, on_click=lambda _: page.go("/access-history")),
                                ft.IconButton(ft.Icons.LOGOUT, tooltip="Sair", icon_color=ft.Colors.WHITE, on_click=lambda _: page.go("/login"))
                            ]
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row([
                                        ft.Text("Dispositivos e Aparelhos Conectados", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                                        ft.ElevatedButton("Histórico de Locais", icon=ft.Icons.TIMELINE, on_click=lambda _: page.go("/location-history"))
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                    device_list_col,
                                ],
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                            ),
                            padding=20,
                            expand=True,
                        )
                    ],
                    # FAB corrigido nativamente sem truncamento de texto
                    floating_action_button=ft.FloatingActionButton(
                        text="Vincular Novo Dispositivo",
                        icon=ft.Icons.ADD,
                        bgcolor=ft.Colors.INDIGO,
                        foreground_color=ft.Colors.WHITE,
                        on_click=lambda _: page.go("/add-device")
                    ),
                )
            )

        # 3. Tela de Adicionar Dispositivo
        elif page.route == "/add-device":
            device_code = ft.TextField(label="Código Único / IMEI", border_radius=8)
            device_name = ft.TextField(label="Nome do Dependente / Aparelho", border_radius=8)
            device_type = ft.Dropdown(
                label="Tipo de Aparelho",
                border_radius=8,
                options=[ft.dropdown.Option("Celular"), ft.dropdown.Option("Relógio")]
            )
            status_text = ft.Text("", color=ft.Colors.GREEN)

            def save_device(e):
                if not device_code.value or not device_name.value or not device_type.value:
                    status_text.value = "Preencha todos os campos obrigatórios!"
                    status_text.color = ft.Colors.RED
                else:
                    page.devices.append({
                        "id": device_code.value,
                        "name": device_name.value,
                        "type": device_type.value,
                        "status": "Online",
                        "battery": "100%"
                    })
                    page.access_log.insert(0, {"user": "Administrador", "action": f"Vinculou novo aparelho: {device_name.value}", "time": datetime.now().strftime("%d/%m/%Y %H:%M")})
                    status_text.value = "Dispositivo vinculado com sucesso!"
                    status_text.color = ft.Colors.GREEN
                    page.go("/dashboard")
                page.update()

            page.views.append(
                ft.View(
                    "/add-device",
                    [
                        ft.AppBar(
                            title=ft.Text("Vincular Novo Dispositivo", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Cadastre um novo rastreador IoT", size=18, weight=ft.FontWeight.BOLD),
                                    device_name,
                                    device_code,
                                    device_type,
                                    ft.ElevatedButton(
                                        text="Salvar e Vincular",
                                        icon=ft.Icons.CHECK,
                                        bgcolor=ft.Colors.INDIGO,
                                        color=ft.Colors.WHITE,
                                        on_click=save_device,
                                        width=250
                                    ),
                                    status_text,
                                ],
                                spacing=20,
                            ),
                            padding=20,
                            expand=True,
                        )
                    ]
                )
            )

        # 4. Tela de Rastreamento (Google Maps Simulator / Leaflet Style View)
        elif page.route == "/tracking":
            page.views.append(
                ft.View(
                    "/tracking",
                    [
                        ft.AppBar(
                            title=ft.Text("Rastreamento Geográfico em Tempo Real", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Mapa Interativo (Simulação IoT)", size=18, weight=ft.FontWeight.BOLD),
                                    # Container simulando a interface do Google Maps com pins de localização
                                    ft.Container(
                                        content=ft.Stack([
                                            ft.Container(bgcolor=ft.Colors.BLUE_GREY_100, expand=True, alignment=ft.alignment.center),
                                            ft.Column([
                                                ft.Row([ft.Icon(ft.Icons.LOCATION_PIN, color=ft.Colors.RED, size=30), ft.Text("João: Escola Estadual (-23.5505, -46.6333)", weight=ft.FontWeight.BOLD, bgcolor=ft.Colors.WHITE70)], alignment=ft.MainAxisAlignment.CENTER),
                                                ft.Container(height=40),
                                                ft.Row([ft.Icon(ft.Icons.LOCATION_PIN, color=ft.Colors.GREEN, size=30), ft.Text("Maria: Parque Ibirapuera (-23.5882, -46.6582)", weight=ft.FontWeight.BOLD, bgcolor=ft.Colors.WHITE70)], alignment=ft.MainAxisAlignment.CENTER),
                                            ], alignment=ft.MainAxisAlignment.CENTER, expand=True)
                                        ]),
                                        height=350,
                                        border_radius=10,
                                        border=ft.border.all(1, ft.Colors.GREY_400)
                                    ),
                                    ft.Text("Últimas Coordenadas Registradas pelos Sensores:", weight=ft.FontWeight.BOLD),
                                    ft.Card(content=ft.Container(content=ft.Column([
                                        ft.ListTile(leading=ft.Icon(ft.Icons.GPS_FIXED, color=ft.Colors.INDIGO), title=ft.Text("João - Precisão Alta (GPS)"), subtitle=ft.Text("Latitude: -23.5505 | Longitude: -46.6333"))
                                    ]), padding=5)),
                                    ft.Card(content=ft.Container(content=ft.Column([
                                        ft.ListTile(leading=ft.Icon(ft.Icons.GPS_FIXED, color=ft.Colors.INDIGO), title=ft.Text("Maria - Precisão Alta (GPS)"), subtitle=ft.Text("Latitude: -23.5882 | Longitude: -46.6582"))
                                    ]), padding=5)),
                                ],
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO
                            ),
                            padding=20,
                            expand=True,
                        )
                    ]
                )
            )

        # 5. Tela de Histórico de Localizações
        elif page.route == "/location-history":
            history_col = ft.Column(spacing=10)
            for item in page.location_history:
                history_col.controls.append(
                    ft.Card(content=ft.Container(content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.HISTORY_EDU, color=ft.Colors.INDIGO),
                        title=ft.Text(f"Dependente: {item['child']} — Local: {item['location']}", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Horário: {item['time']} | Coordenadas: {item['coords']}")
                    ), padding=5))
                )

            page.views.append(
                ft.View(
                    "/location-history",
                    [
                        ft.AppBar(
                            title=ft.Text("Histórico de Localizações", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Linha do tempo de deslocamento das crianças", size=18, weight=ft.FontWeight.BOLD),
                                history_col
                            ], spacing=15, scroll=ft.ScrollMode.AUTO),
                            padding=20, expand=True
                        )
                    ]
                )
            )

        # 6. Tela de Histórico de Acessos
        elif page.route == "/access-history":
            log_col = ft.Column(spacing=10)
            for log in page.access_log:
                log_col.controls.append(
                    ft.Card(content=ft.Container(content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.SECURITY_UPDATE_GOOD, color=ft.Colors.BLUE),
                        title=ft.Text(f"Usuário: {log['user']}", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Ação: {log['action']} \nData/Hora: {log['time']}")
                    ), padding=5))
                )

            page.views.append(
                ft.View(
                    "/access-history",
                    [
                        ft.AppBar(
                            title=ft.Text("Histórico de Acessos ao Painel", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Registro de entradas, saídas e auditoria", size=18, weight=ft.FontWeight.BOLD),
                                log_col
                            ], spacing=15, scroll=ft.ScrollMode.AUTO),
                            padding=20, expand=True
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
