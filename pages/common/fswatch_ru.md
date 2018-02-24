# fswatch

> Кросс-платформенный мониторинг изменений в файлах.

- Запускает bash-команду при создании, обновлении или удалении файла:

`fswatch -0 {{path/to/file}} | xargs -0 {{bash_command}}`

- Наблюдает за одним или несколькими файлами и/или папками:

`fswatch -0 {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -0 {{bash_command}}`

- Используйте `{}` в bash-команде для подстановки абсолютного пути к измененному файлу:

`fswatch -0 {{path/to/directory}} | xargs -0 -I {} {{bash_command}}`

- Выбрать типы событий, например, Обновлено (Updated), Удалено (Deleted) или Создано (Created):

`fswatch -0 --event {{Updated}} {{path/to/directory}} | xargs -0 {{bash_command}}`
