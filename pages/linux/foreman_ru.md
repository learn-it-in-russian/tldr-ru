# foreman

> Менеджер приложений, использующих Procfile.

- Запустить приложение с Procfile в текущей директории:

`foreman start`

- Запустить приложение с указанным Procfile-ом:

`foreman start -f {{Procfile}}`

- Запустить указанное приложение:

`foreman start {{process}}`

- Проверить Procfile на ошибки:

`foreman check`

- Запустить одну команду с окружением процесса:

`foreman run {{command}}`

- Запустить все процессы, за исключением процесса "worker":

`foreman start -m all=1,{{worker}}=0`
