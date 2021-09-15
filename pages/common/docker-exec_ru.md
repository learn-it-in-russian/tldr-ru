# docker exec

> Запустить команду в уже запущенном Docker контейнере

- Войти в интерактивный режим командной строки `bash` в уже запущенном контейнере:

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- Запустить команду в фоне (не захватывая терминал) в работающем контейнере:

`docker exec --detach {{container_name}} {{command}}`

- Выбрать рабочую директорию для данной команды и запустить её там:

`docker exec --interactive -tty --workdir {{path/to/directory}} {{container_name}} {{command}}`

- Запустить команду в фоне (не захватывая терминал) в работающем контейнере, но оставить ввод (stdin) открытым:

`docker exec --interactive --detach {{container_name}} {{command}}`

- Установить переменную окружения в запущенной `bash` сессии:

`docker exec --interactive --tty --env {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Запустить команду от имени указанного пользователя:

`docker exec --user {{user}} {{container_name}} {{command}}`
