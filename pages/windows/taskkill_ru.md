# taskkill

> Завершить процесс по идентификатору или имени процесса.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- Завершить процесс по его идентификатору:

`taskkill /pid {{process_id}}`

- Завершить процесс по его имени:

`taskkill /im {{process_name}}`

- Принудительно завершить процесс по его идентификатору:

`taskkill /pid {{process_id}} /f`

- Завершить процесс и его дочерние процессы:

`taskkill /im {{process_name}} /t`

- Завершить процесс на удаленной системе:

`taskkill /pid {{process_id}} /s {{remote_name}}`

- Отобразить информацию об использовании этой команды:

`taskkill /?`
