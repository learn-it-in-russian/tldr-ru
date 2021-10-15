# git remote

> Управление набором отслеживаемых репозиториев («удаленных репозиториев»).

- Показать список существующих удаленных репозиториев, их имена и URL:

`git remote -v`

- Добавить удаленный репозиторий:

`git remote add {{remote_name}} {{remote_url}}`

- Изменение URL-адреса удаленного репозитория:

`git remote set-url {{remote_name}} {{new_url}}`

- Удаление удаленного репозитория:

`git remote remove {{remote_name}}`

- Переименование удаленного репозитория:

`git remote rename {{old_name}} {{new_name}}`