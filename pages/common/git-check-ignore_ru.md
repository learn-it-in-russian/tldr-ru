# git check-ignore

> Анализ и отладка игнорируемых/исключённых из Git репозитория файлов (".gitignore").

- Проверяет, игнорируется ли файл или каталог:

`git check-ignore {{path/to/file_or_directory}}`

- Проверят несколько файлов или директорий - игнорируются ли они по правилам `.gitignore`:

`git check-ignore {{path/to/file}} {{path/to/directory}}`

- Использовать файл с путями до файлов (один на строку) для проверки, игнорируются ли они:

`git check-ignore --stdin < {{path/to/file_list}}`

- Не проверять индекс Git (используется для отладки: почему файлы или директории отслеживались, а не игнорировались):

`git check-ignore --no-index {{path/to/files_or_directories}}`

- Выводить подробную информацию о шаблонах `.gitignore`, по которым игнорируется файл или директория:

`git check-ignore --verbose {{path/to/files_or_directories}}`
