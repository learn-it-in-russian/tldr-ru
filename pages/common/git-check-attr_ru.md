# git check-attr

> Для каждого пути до файла выводит/устанавливает/сбрасывает Git атрибут.

- Проверить значение всех атрибутов файла:

`git check-attr --all {{path/to/file}}`

- Проверить значение указанного атрибута файла:

`git check-attr {{attribute}} {{path/to/file}}`

- Проверить значения всех атрибутов для нескольких файлов:

`git check-attr --all {{path/to/file1}} {{path/to/file2}}`

- Для нескольких файлов проверить значение конкретного аттрибута:

`git check-attr {{attribute}} {{path/to/file1}} {{path/to/file2}}`
