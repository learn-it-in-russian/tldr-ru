# findmnt

> Найти ваши файловые системы.

- Отобразить список всех примонтированных файловых систем:

`findmnt`

- Поиск по устройству:

`findmnt {{/dev/sdb1}}`

- Поиск по точке монтирования:

`findmnt {{/}}`

- Поиск по типу файловой системы:

`findmnt -t {{ext4}}`

- Поиск по метке устройства:

`findmnt LABEL={{BigStorage}}`