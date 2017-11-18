# ifconfig

> Программа настройки сетевых интерфейсов (Network Interface Configurator).

- Вывести сетевые настройки Ethernet-адаптера:

`ifconfig eth0`

- Показать настройки всех интерфесов, даже отключенных:

`ifconfig -a`

- Отключить интерфейс eth0:

`ifconfig eth0 down`

- Включить интерфейс eth0:

`ifconfig eth0 up`

- Назначить IP-адрес интерфейсу eth0:

`ifconfig eth0 {{ip_address}}`
