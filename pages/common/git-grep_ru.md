# git-grep

> Найти строки внутри файлов в истории репозитория.
> Принимает многие ключи, что и утилита `grep`.

- Поиск строки в закоммиченных файлах:

`git grep {{search_string}}`

- Поиск строки а файлах, подходящих под указанный шаблон:

`git grep {{search_string}} -- {{file_glob_pattern}}`

- Поиск строки в закоммиченых файлах, включая Git подмодули:

`git grep --recurse-submodules {{search_string}}`

- Поиск по строке внутри указанного коммита (точки из истории репозитория):

`git grep {{search_string}} {{HEAD~2}}`

- Поиск строки среди всех веток:

`git grep {{search_string}} $(git rev-list --all)`
