import flet as ft

def main(page: ft.Page):
    page.title = "SafeChild IoT - Pais"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.INDIGO_50

    def fetch_location():
        return {
            "device_id": "esp32_crianca_01",
            "latitude": -23.550520,
            "longitude": -46.633308,
            "timestamp": "Online agora",
            "status": "Ativo"
        }

    # ================= TELA DE LOGIN =================
    def show_login(e=None):
        email_ctrl = ft.TextField(label="E-mail do Responsável", border=ft.InputBorder.OUTLINE, width=300)
        pass_ctrl = ft.TextField(label="Senha", password=True, can_reveal_password=True, border=ft.InputBorder.OUTLINE, width=300)
        
        def handle_login(evt):
            if email_ctrl.value and pass_ctrl.value:
                show_dashboard()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha e-mail e senha."))
                page.snack_bar.open = True
                page.update()

        page.clean()
        page.add(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.Icons.SECURITY, size=64, color=ft.Colors.INDIGO),
                        ft.Text("SafeChild IoT", size=24, weight="bold", color=ft.Colors.INDIGO),
                        ft.Text("Área de Monitoramento dos Pais", color=ft.Colors.GREY_700),
                        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                        email_ctrl,
                        pass_ctrl,
                        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                        ft.ElevatedButton(
                            "Entrar", 
                            on_click=handle_login, 
                            bgcolor=ft.Colors.INDIGO, 
                            color=ft.Colors.WHITE, 
                            width=300
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                    padding=30,
                ),
                elevation=6,
            )
        )
        page.update()

    # ================= DASHBOARD =================
    def show_dashboard():
        def go_to_tracking(evt):
            show_tracking()

        def go_to_add(evt):
            show_add_device()

        page.clean()
        page.add(
            ft.AppBar(
                title=ft.Text("Meus Filhos Monitorados"),
                bgcolor=ft.Colors.INDIGO,
                color=ft.Colors.WHITE,
                actions=[
                    ft.IconButton(ft.Icons.LOGOUT, on_click=show_login, icon_color=ft.Colors.WHITE)
                ]
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Dispositivos Conectados", size=18, weight="bold", color=ft.Colors.BLACK87),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    ft.Card(
                        content=ft.ListTile(
                            leading=ft.CircleAvatar(content=ft.Icon(ft.Icons.CHILD_CARE, color=ft.Colors.WHITE), bgcolor=ft.Colors.INDIGO),
                            title=ft.Text("Lucas Almeida", weight="bold"),
                            subtitle=ft.Text("ID: esp32_crianca_01\nStatus: Ativo"),
                            is_three_line=True,
                            trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16),
                            on_click=go_to_tracking,
                        ),
                        elevation=3,
                    ),
                ]),
                padding=20,
                expand=True,
            ),
            ft.FloatingActionButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.ADD, color=ft.Colors.WHITE),
                    ft.Text("Vincular Novo Dispositivo", color=ft.Colors.WHITE)
                ], tight=True),
                bgcolor=ft.Colors.INDIGO,
                on_click=go_to_add
            )
        )
        page.update()

    # ================= TELA DE CADASTRO =================
    def show_add_device():
        name_ctrl = ft.TextField(label="Nome da Criança", border=ft.InputBorder.OUTLINE)
        id_ctrl = ft.TextField(label="ID do Hardware (ex: esp32_02)", border=ft.InputBorder.OUTLINE)

        def save_device(evt):
            page.snack_bar = ft.SnackBar(ft.Text("Dispositivo vinculado com sucesso!"))
            page.snack_bar.open = True
            page.update()
            show_dashboard()

        page.clean()
        page.add(
            ft.AppBar(
                title=ft.Text("Vincular Dispositivo IoT"), 
                bgcolor=ft.Colors.INDIGO, 
                color=ft.Colors.WHITE,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_dashboard(), icon_color=ft.Colors.WHITE)
            ),
            ft.Container(
                content=ft.Column([
                    name_ctrl,
                    id_ctrl,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    ft.ElevatedButton(
                        "Salvar e Vincular", 
                        on_click=save_device, 
                        bgcolor=ft.Colors.INDIGO, 
                        color=ft.Colors.WHITE, 
                        width=float("inf")
                    )
                ], spacing=15),
                padding=20,
                expand=True
            )
        )
        page.update()

    # ================= TELA DE RASTREAMENTO =================
    def show_tracking():
        data = fetch_location()
        
        lat_text = ft.Text(f"Latitude: {data['latitude']}")
        lon_text = ft.Text(f"Longitude: {data['longitude']}")
        time_text = ft.Text(f"Última Att: {data['timestamp']}")
        status_chip = ft.Chip(label=ft.Text(data['status'], color=ft.Colors.WHITE), bgcolor=ft.Colors.GREEN)

        def refresh_data(evt):
            new_data = fetch_location()
            lat_text.value = f"Latitude: {new_data['latitude']}"
            lon_text.value = f"Longitude: {new_data['longitude']}"
            time_text.value = f"Última Att: {new_data['timestamp']}"
            page.update()

        maps_url = f"https://www.google.com/maps/search/?api=1&query={data['latitude']},{data['longitude']}"

        page.clean()
        page.add(
            ft.AppBar(
                title=ft.Text(f"Rastreando: {data['device_id']}"), 
                bgcolor=ft.Colors.INDIGO, 
                color=ft.Colors.WHITE,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_dashboard(), icon_color=ft.Colors.WHITE)
            ),
            ft.Container(
                content=ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("Localização em Tempo Real", size=20, weight="bold", color=ft.Colors.INDIGO),
                                ft.Divider(color=ft.Colors.INDIGO_100),
                                ft.Text(f"Dispositivo: {data['device_id']}"),
                                lat_text,
                                lon_text,
                                time_text,
                                ft.Row([ft.Text("Status: "), status_chip]),
                                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                ft.ElevatedButton(
                                    "Abrir no Google Maps", 
                                    icon=ft.Icons.MAP, 
                                    url=maps_url, 
                                    bgcolor=ft.Colors.INDIGO, 
                                    color=ft.Colors.WHITE, 
                                    width=float("inf")
                                )
                            ], spacing=10),
                            padding=24,
                        ),
                        elevation=4
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                padding=20,
                expand=True
            ),
            ft.FloatingActionButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.REFRESH, color=ft.Colors.WHITE),
                    ft.Text("Atualizar", color=ft.Colors.WHITE)
                ], tight=True),
                bgcolor=ft.Colors.INDIGO,
                on_click=refresh_data,
                tooltip="Atualizar Posição"
            )
        )
        page.update()

    show_login()

if __name__ == "__main__":
    ft.app(target=main)
