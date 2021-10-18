# find

> Найти указанную строку в одном или нескольких файлах.
> Больше информации: <https://docs.microsoft.com/windows-server/administration/windows-commands/find>.

- Найти строки содержащие указанную строку:

`find {{string}} {{path/to/file_or_directory}}`

- Отобразить строки в файле, не содержащие указанную строку:

`find {{string}} {{path/to/file_or_directory}} /v`

- Показать количество строк, содержащих указанную строку:

`find {{string}} {{path/to/file_or_directory}} /c`

- Отобразить найденные строки с их номерами:

`find {{string}} {{path/to/file_or_directory}} /n`
