# a2query

> Извлечение конфигурации среды выполнения из Apache в операционных системах на базе Debian.
> More information: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Список включенных модулей Apache:

`sudo a2query -m`

- Проверяется, установлен ли определенный модуль:

`sudo a2query -m {{module_name}}`

- Список включенных виртуальных хостов:

`sudo a2query -s`

- Отображение включенного в данный момент Модуля Множественной Обработки:

`sudo a2query -M`

- Отображение версии Apache:

`sudo a2query -v`
