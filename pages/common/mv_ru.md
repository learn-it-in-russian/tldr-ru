# mv

> Перемещает или переименовывает файлы и директории.

- Перемещает файл или папку из `{{source}}` в `{{target}}`:

`mv {{source}} {{target}}`

- Перемещает файлы в другую директорию, сохраняя имена:

`mv {{source1}} {{source2}} {{source3}} {{target_directory}}`

- Перемещать, не спрашивая подтверждение на перезапись уже существующих файлов:

`mv -f {{source}} {{target}}`

- Запросить подтверждение перед перезаписью существующих файлов, независимо от прав доступа к файлам:

`mv -i {{source}} {{target}}`

- Переместить, не перезаписывая уже имеющиеся файлы по целевому пути:

`mv -n {{source}} {{target}}`

- Перемещать файлы в подробном режиме: печатать каждый файл после его перемещения:

`mv -v {{source}} {{target}}`