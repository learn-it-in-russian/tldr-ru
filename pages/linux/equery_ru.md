# equery

> Утилита для отображения информации об установленных пакетах в Gentoo Linux.

- Список всех установленных пакетов:

`equery list '*'`

- Поиск пакета в дереве Portage и в оверлеях:

`equery list -po {{package_name}}`

- Список всех пакетов, которые зависят от данного пакета:

`equery depends {{package_name}}`

- Список всех пакетов, от которых зависит данный пакет:

`equery depgraph {{package_name}}`

- Список всех файлов установленных пакетом:

`equery files --tree {{package_name}}`
