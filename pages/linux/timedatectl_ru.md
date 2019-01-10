# timedatectl

> Управление системным временем и датой.

- Проверка текущего времени системных часов:

`timedatectl`

- Установка локального времени системы напрямую:

`timedatectl set-time {{"yyyy-MM-dd hh:mm:ss"}}`

- Просмотр доступных временных зон:

`timedatectl list-timezones`

- Смена временной зоны:

`timedatectl set-timezone {{timezone}}`

- Включение синхронизации с Протоколом Сетевого Времени (NTP):

`timedatectl set-ntp on`
