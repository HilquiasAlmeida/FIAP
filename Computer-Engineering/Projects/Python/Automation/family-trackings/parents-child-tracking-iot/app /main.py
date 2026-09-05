import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Family Trackings IoT - Painel Pais & Filhos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # ---------------------------------------------------------
    # BANCO DE DADOS EM MEMÓRIA (Mantido e Expandido)
    # ---------------------------------------------------------
    if not hasattr(page, "devices"):
        page.devices = [
            {"id": "IMEI-987654321", "name": "João", "equipment": "Smartphone Samsung", "status": "Online", "battery": "85%", "lat": "-23.5505", "lng": "-46.6333", "location": "Escola Estadual"},
            {"id": "IMEI-123456789", "name": "Maria", "equipment": "Smartwatch Apple", "status": "Online", "battery": "62%", "lat": "-23.5882", "lng": "-46.6582", "location": "Parque Ibirapuera"}
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

    if not hasattr(page, "general_history"):
        page.general_history = [
            {"title": "Sistema Inicializado", "desc": "Painel carregado com sucesso.", "time": datetime.now().strftime("%d/%m/%Y %H:%M"), "type": "system"}
        ]

    if not hasattr(page, "selected_device"):
        page.selected_device = page.devices[0]

    def route_change(e):
        page.views.clear()
        
        # ---------------------------------------------------------
        # 1. TELA DE LOGIN
        # ---------------------------------------------------------
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
                    page.general_history.insert(0, {"title": "Acesso ao Sistema", "desc": f"Usuário {user_field.value} fez login", "time": datetime.now().strftime("%d/%m/%Y %H:%M"), "type": "auth"})
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
                                    ft.Text("Painel de Monitoramento Familiar", size=14, color=ft.Colors.GREY_700),
                                    ft.Container(height=10),
                                    user_field,
                                    pass_field,
                                    ft.ElevatedButton(
                                        text="Entrar no Sistema",
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

        # ---------------------------------------------------------
        # 2. TELA PRINCIPAL / DASHBOARD
        # ---------------------------------------------------------
        elif page.route == "/dashboard":
            device_list_col = ft.Column(spacing=10)

            def open_real_map(dev):
                page.selected_device = dev
                page.go("/map-view")

            def refresh_devices():
                device_list_col.controls.clear()
                if not page.devices:
                    device_list_col.controls.append(ft.Text("Nenhum dispositivo cadastrado.", color=ft.Colors.GREY_600))
                for dev in page.devices:
                    device_list_col.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.PHONE_ANDROID if 'Smartphone' in dev['equipment'] else ft.Icons.WATCH, color=ft.Colors.INDIGO),
                                        title=ft.Text(f"Criança: {dev['name']} ({dev['equipment']})", weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text(f"Série/IMEI: {dev['id']} • Status: {dev['status']} • Bateria: {dev['battery']}\nLocal Atual: {dev.get('location', 'Desconhecido')}"),
                                    ),
                                    ft.Row([
                                        ft.TextButton("Excluir", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=lambda e, d=dev: delete_dev(d['id'])),
                                        # BOTÃO QUE ABRE O GOOGLE MAPS REAL INTEGRADO
                                        ft.ElevatedButton("Ver no Google Maps Real", icon=ft.Icons.MAP, bgcolor=ft.Colors.INDIGO, color=ft.Colors.WHITE, on_click=lambda e, d=dev: open_real_map(d)),
                                    ], alignment=ft.MainAxisAlignment.END)
                                ]),
                                padding=10
                            )
                        )
                    )
                page.update()

            def delete_dev(dev_id):
                page.devices = [d for d in page.devices if d["id"] != dev_id]
                page.access_log.insert(0, {"user": "Administrador", "action": f"Removeu dispositivo ID {dev_id}", "time": datetime.now().strftime("%d/%m/%Y %H:%M")})
                page.general_history.insert(0, {"title": "Dispositivo Removido", "desc": f"ID: {dev_id} foi excluído do sistema", "time": datetime.now().strftime("%d/%m/%Y %H:%M"), "type": "device"})
                refresh_devices()

            refresh_devices()

            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.AppBar(
                            title=ft.Text("Painel Familiar - IoT Trackings", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.INDIGO,
                            center_title=True,
                            actions=[
                                ft.IconButton(ft.Icons.HISTORY, tooltip="Central de Históricos", icon_color=ft.Colors.WHITE, on_click=lambda _: page.go("/history-hub")),
                                ft.IconButton(ft.Icons.LOGOUT, tooltip="Sair", icon_color=ft.Colors.WHITE, on_click=lambda _: page.go("/login"))
                            ]
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row([
                                        ft.Text("Dispositivos e Filhos Monitorados", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                                        ft.ElevatedButton("Central de Históricos", icon=ft.Icons.HISTORY_EDU, bgcolor=ft.Colors.INDIGO_LIGHT, color=ft.Colors.INDIGO_900, on_click=lambda _: page.go("/history-hub"))
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
                    floating_action_button=ft.FloatingActionButton(
                        text="+ Vincular Novo Dispositivo",
                        icon=ft.Icons.ADD,
                        bgcolor=ft.Colors.INDIGO,
                        foreground_color=ft.Colors.WHITE,
                        on_click=lambda _: page.go("/add-device")
                    ),
                )
            )

        # ---------------------------------------------------------
        # 3. TELA DE ADICIONAR DISPOSITIVO
        # ---------------------------------------------------------
        elif page.route == "/add-device":
            child_name_field = ft.TextField(label="Nome da Criança", border_radius=8, prefix_icon=ft.Icons.PERSON)
            equipment_field = ft.TextField(label="Equipamento (Ex: Smartphone, Smartwatch)", border_radius=8, prefix_icon=ft.Icons.PHONE_ANDROID)
            serial_field = ft.TextField(label="Número de Série / IMEI", border_radius=8, prefix_icon=ft.Icons.CONFIRMATION_NUMBER)
            status_text = ft.Text("", color=ft.Colors.GREEN)

            def save_device(e):
                if not child_name_field.value or not equipment_field.value or not serial_field.value:
                    status_text.value = "Preencha todos os campos obrigatórios!"
                    status_text.color = ft.Colors.RED
                else:
                    new_item = {
                        "id": serial_field.value,
                        "name": child_name_field.value,
                        "equipment": equipment_field.value,
                        "status": "Online",
                        "battery": "100%",
                        "lat": "-23.5505",
                        "lng": "-46.6333",
                        "location": "Residência / Padrão"
                    }
                    page.devices.append(new_item)
                    page.location_history.insert(0, {"child": child_name_field.value, "location": "Residência / Padrão", "time": "Agora mesmo", "coords": "-23.5505, -46.6333"})
                    page.general_history.insert(0, {"title": "Novo Dispositivo Vinculado", "desc": f"Criança: {child_name_field.value} | Aparelho: {equipment_field.value} | Série: {serial_field.value}", "time": datetime.now().strftime("%d/%m/%Y %H:%M"), "type": "device"})
                    
                    status_text.value = "Dispositivo salvo com sucesso!"
                    status_text.color = ft.Colors.GREEN
                    page.update()
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
                                    ft.Text("Informe os dados da criança e do hardware IoT", size=16, weight=ft.FontWeight.BOLD),
                                    child_name_field,
                                    equipment_field,
                                    serial_field,
                                    ft.ElevatedButton(
                                        text="Salvar e Vincular Aparelho",
                                        icon=ft.Icons.CHECK,
                                        bgcolor=ft.Colors.INDIGO,
                                        color=ft.Colors.WHITE,
                                        on_click=save_device,
                                        width=280
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

        # ---------------------------------------------------------
        # 4. TELA DE MAPA REAL (GOOGLE MAPS INTEGRADO COM O NOME DA CRIANÇA)
        # ---------------------------------------------------------
        elif page.route == "/map-view":
            dev = page.selected_device
            map_url = f"https://maps.google.com/maps?q={dev['lat']},{dev['lng']}&z=15&output=embed"
            
            try:
                map_component = ft.WebView(url=map_url, expand=True)
            except Exception:
                map_component = ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.Icons.MAP, size=64, color=ft.Colors.INDIGO),
                        ft.Text(f"Visualizando mapa para: {dev['name']}", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Local: {dev['location']} ({dev['lat']}, {dev['lng']})", size=14),
                        ft.ElevatedButton("Abrir no Navegador Externo", icon=ft.Icons.OPEN_IN_NEW, on_click=lambda _: page.launch_url(f"https://www.google.com/maps/search/?api=1&query={dev['lat']},{dev['lng']}"))
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    expand=True
                )

            page.views.append(
                ft.View(
                    "/map-view",
                    [
                        ft.AppBar(
                            title=ft.Text(f"Google Maps - {dev['name']}", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Container(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED, size=30),
                                        ft.Column([
                                            ft.Text(f"Criança Monitorada: {dev['name']}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                                            ft.Text(f"Localização Atual: {dev['location']} • Coordenadas: {dev['lat']}, {dev['lng']}", size=13, color=ft.Colors.GREY_700),
                                        ], spacing=2)
                                    ], alignment=ft.MainAxisAlignment.START),
                                    bgcolor=ft.Colors.INDIGO_50,
                                    padding=15,
                                    border_radius=10,
                                ),
                                ft.Container(
                                    content=map_component,
                                    expand=True,
                                    border=ft.border.all(1, ft.Colors.INDIGO_200),
                                    border_radius=10,
                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS
                                )
                            ], spacing=10),
                            padding=15,
                            expand=True
                        )
                    ]
                )
            )

        # ---------------------------------------------------------
        # 5. CENTRAL DE HISTÓRICOS
        # ---------------------------------------------------------
        elif page.route == "/history-hub":
            general_col = ft.Column(spacing=8)
            for item in page.general_history:
                general_col.controls.append(
                    ft.Card(content=ft.Container(content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.TIMELINE, color=ft.Colors.INDIGO),
                        title=ft.Text(item['title'], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"{item['desc']}\nHorário: {item['time']}")
                    ), padding=5))
                )

            individual_col = ft.Column(spacing=8)
            for loc in page.location_history:
                individual_col.controls.append(
                    ft.Card(content=ft.Container(content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED),
                        title=ft.Text(f"Filho(a): {loc['child']} - Local: {loc['location']}", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Tempo: {loc['time']} | Coordenadas: {loc['coords']}")
                    ), padding=5))
                )

            access_col = ft.Column(spacing=8)
            for log in page.access_log:
                access_col.controls.append(
                    ft.Card(content=ft.Container(content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.SECURITY, color=ft.Colors.BLUE),
                        title=ft.Text(f"Usuário: {log['user']}", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Ação: {log['action']} | Data: {log['time']}")
                    ), padding=5))
                )

            page.views.append(
                ft.View(
                    "/history-hub",
                    [
                        ft.AppBar(
                            title=ft.Text("Central de Históricos - Pais & Mães", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.INDIGO,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"), icon_color=ft.Colors.WHITE),
                        ),
                        ft.Container(
                            content=ft.Tabs(
                                selected_index=0,
                                animation_duration=300,
                                tabs=[
                                    ft.Tab(
                                        text="Histórico Geral",
                                        icon=ft.Icons.ALL_INBOX,
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.Text("Todos os eventos consolidados do sistema:", size=16, weight=ft.FontWeight.BOLD),
                                                general_col
                                            ], spacing=15, scroll=ft.ScrollMode.AUTO),
                                            padding=15
                                        ),
                                    ),
                                    ft.Tab(
                                        text="Históricos Individuais (Filhos)",
                                        icon=ft.Icons.PERSON,
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.Text("Histórico específico de deslocamento por dependente:", size=16, weight=ft.FontWeight.BOLD),
                                                individual_col
                                            ], spacing=15, scroll=ft.ScrollMode.AUTO),
                                            padding=15
                                        ),
                                    ),
                                    ft.Tab(
                                        text="Acessos e Auditoria",
                                        icon=ft.Icons.SECURITY_UPDATE_GOOD,
                                        content=ft.Container(
                                            content=ft.Column([
                                                ft.Text("Log de logins e alterações de segurança:", size=16, weight=ft.FontWeight.BOLD),
                                                access_col
                                            ], spacing=15, scroll=ft.ScrollMode.AUTO),
                                            padding=15
                                        ),
                                    ),
                                ],
                                expand=True,
                            ),
                            padding=10,
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
