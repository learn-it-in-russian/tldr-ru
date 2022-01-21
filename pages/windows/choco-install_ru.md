# choco install

> Установить один или больее пакетов Chocolatey.

- Установить пакет, или несколько (разделяются пробелом):

`choco install {{package(s)}}`

- Установить пакет, используя указанный файл конфигурации:

`choco install {{path/to/packages.config}}`

- Установить пакет, используя nuspec или nupkg файл:

`choco install {{path/to/file}}`

- Установить пакет указанной версии:

`choco install {{package}} --version {{version}}`

- Разрешить установку нескольких версий одного пакета:

`choco install {{package}} --allow-multiple`

- Согласиться со всеми задаваемыми при установке вопросами автоматически:

`choco install {{package}} --yes`

- Указать репозиторий для получения пакета:

`choco install {{package}} --source {{source_url|alias}}`

- Задать логин и пароль для аутентификации:

`choco install {{package}} --user {{username}} --password {{password}}`
