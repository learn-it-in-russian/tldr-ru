# xattr

> Утилита для работы с расширенными атрибутами файловой системы.

- Отобразить список пар: ключ: значение расширенных атрибутов для данного файла:

`xattr -l {{file}}`

- Добавить атрибут в заданный файл:

`xattr -w {{attribute_key}} {{attribute_value}} {{file}}`

- Удалить атрибут из заданного файла:

`xattr -d {{attribute_key}} {{file}}`

- Удалить все расширенные атрибуты из заданного файла:

`xattr -c {{file}}`

- Рекурсивно удалить все атрибуты в данной директории:

`xattr -rd {{attribute_key}} {{directory}}`