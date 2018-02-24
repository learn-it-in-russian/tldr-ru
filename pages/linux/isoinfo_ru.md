# isoinfo

> Утилита для копирования и проверки ISO-образов дисков.

- Вывести список всех файлов включенных в ISO-образ:

`isoinfo -f -i {{path/to/image.iso}}`

- Извлечь определенный файл из ISO-образа и направить его на стандартный вывод:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- Отобразить информацию заголовка ISO-образа:

`isoinfo -d -i {{path/to/image.iso}}`
