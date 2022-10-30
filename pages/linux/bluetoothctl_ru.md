# bluetoothctl

> Программа для управления устройствами Bluetooth из командной строки.

- Войти в командную оболочку `bluetoothctl`:

`bluetoothctl`

- Вывести список всех известных устройств:

`bluetoothctl devices`

- Включить / выключить Bluetooth контроллер:

`bluetoothctl power {{on|off}}`

- Присоединить устройство bluetooth по MAC-адресу:

`bluetoothctl pair {{mac_address}}`

- Отключить bluetooth устройство по указанному MAC-адресу:

`bluetoothctl remove {{mac_address}}`

- Подключиться к присоединённому устройству:

`bluetoothctl connect {{mac_address}}`

- Отключиться от присоединённого устройства:

`bluetoothctl disconnect {{mac_address}}`

- Вывести справочную информацию о программе:

`bluetoothctl help`
