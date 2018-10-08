# git checkout

> Использовать одну из git-веток в качестве рабочей.

- Создать и переключиться на новую ветку:

`git checkout -b {{branch_name}}`

- Переключиться на существующую локальную ветку:

`git checkout {{branch_name}}`

- Переключиться на существующую удалённую git-ветку (скачать с сервера):

`git checkout --track {{remote_name}}/{{branch_name}}`

- Отменить все незафиксированные изменения в текущей директории (также смотри [git reset](https://900913.ru/tldr/common/en/git-reset/)):

`git checkout .`

- Отменить все незафиксированные изменения в указанном файле:

`git checkout {{file_name}}`

- Заменить файл в текущей директории версией этого файла из другой ветки:

`git checkout {{branch_name}} -- {{file_name}}`
