# choco list

> Вывести список пакетов Chocolatey.

- Вывести все доступные пакеты:

`choco list`

- Вывести все установленные локально пакеты:

`choco list --local-only`

- Вывести список пакетов, включая локальные программы:

`choco list --include-programs`

- Вывести только подтверждённые пакеты:

`choco list --approved-only`

- Указать специальный репозиторий для просмотра пакетов:

`choco list --source {{source_url|alias}}`

- Задать логин и пароль для аутентификации:

`choco list --user {{username}} --password {{password}}`
