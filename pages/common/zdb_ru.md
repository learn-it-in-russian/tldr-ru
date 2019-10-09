# zdb

> ZFS отладчик.

- Показать подробную конфигурацию всех смонтированных ZFS z-пулов:

`zdb`

- Показать подробную конфигурацию для определенного пула ZFS:

`zdb -C {{poolname}}`

- Show statistics about number, size and deduplication of blocks:

`zdb -b {{poolname}}`
