# zfs

> Управление файловой системой ZFS.

- Список всех доступных файловых систем zfs:

`zfs list`

- Создание новой файловой системы ZFS:

`zfs create {{pool_name/filesystem_name}}`

- Удалить файловую систему ZFS:

`zfs destroy {{pool_name/filesystem_name}}`

- Создание снимка файловой системы ZFS:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Включение сжатия в файловой системе:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Изменение точки монтирования для файловой системы:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
