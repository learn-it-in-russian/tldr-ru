# losetup

> Установка и настройка петлевых устройств.

- Список loop-устройств с подробной информацией:

`losetup -a`

- Привязать файл к loop-устройству:

`sudo losetup /dev/{{loop}} /{{path/to/file}}`

- Отвязать все loop-устройства:

`sudo losetup -D`

- Отвязать указанное loop-устройство:

`sudo losetup -d /dev/{{loop}}`
