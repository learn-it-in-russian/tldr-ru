# rfkill

> Включает и отключает беспроводные устройства.

- Выводит список устройств:

`rfkill`

- Отфильтровать по колонкам:

`rfkill -o {{ID,TYPE,DEVICE}}`

- Блокировать устройства по типу (например, bluetooth, wlan):

`rfkill block {{bluetooth}}`

- Разблокировать устройства по типу (например, bluetooth, wlan):

`rfkill unblock {{wlan}}`

- Вывести в JSON формате:

`rfkill -J`
