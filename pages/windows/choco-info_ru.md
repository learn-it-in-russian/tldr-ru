# choco info

> Вывести подробную информацию об указанном пакете Chocolatey.

- Показать информацию об указанном пакете:

`choco info {{package}}`

- Вывести информацию только для локального пакета:

`choco info {{package}} --local-only`

- Указать источник пакета и вывести информацию:

`choco info {{package}} --source {{source_url|alias}}`

- Задать логин и пароль для аутентификации:

`choco info {{package}} --user {{username}} --password {{password}}`
