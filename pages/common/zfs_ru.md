# zfs

> Управление файловыми системами ZFS.

- Список всех доступных файловых систем zfs:

`zfs list`

- Создать новую файловую систему ZFS:

`zfs create {{pool_name/filesystem_name}}`

- Удалить файловую систему ZFS:

`zfs destroy {{pool_name/filesystem_name}}`

- Create a Snapshot of a ZFS filesystem:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Enable compression on a filesystem:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Change mountpoint for a filesystem:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
