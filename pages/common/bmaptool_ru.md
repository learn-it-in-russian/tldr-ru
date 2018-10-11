# bmaptool

> Интеллектуальное (и поэтому быстрее чем `cp` или `dd`) создание или копирование blockmap.

- Создаёт blockmap из файла-образа:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- Копирует образ на sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- Копирует сжатый образ на sdb:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- Копирует образ на sdb без использования blockmap:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`
