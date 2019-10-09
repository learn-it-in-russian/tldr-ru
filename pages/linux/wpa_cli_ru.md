# wpa_cli

> Добавление и конфигурирование WLAN интерфейсов.

- Сканирование доступных сетей:

`wpa_cli scan`

- Показ результатов сканирования:

`wpa_cli scan_results`

- Добавление сети:

`wpa_cli add_network {{number}}`

- Установить SSID сети:

`wpa_cli set_network {{number}} ssid "{{SSID}}"`

- Включить сеть:

`wpa_cli enable_network {{number}}`

- Сохранить конфигурацию:

`wpa_cli save_config`
