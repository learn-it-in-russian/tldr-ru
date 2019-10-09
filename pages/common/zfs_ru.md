# zfs

> Manage ZFS filesystems.

- List all available zfs filesystems:

`zfs list`

- Create a new ZFS filesystem:

`zfs create {{pool_name/filesystem_name}}`

- Delete a ZFS filesystem:

`zfs destroy {{pool_name/filesystem_name}}`

- Создать снимок файловой системы ZFS:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Включить сжатие в файловой системе:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Изменить точку монтирования для файловой системы:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
