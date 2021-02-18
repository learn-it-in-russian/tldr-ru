# git instaweb

> Программа для запуска gitweb сервера.

- Запустить gitweb сервер для текущего Git репозитория:

`git instaweb --start`

- Принимать запросы только локально (localhost):

`git instaweb --start --local`

- Запустить сервер на указанном порте:

`git instaweb --start --port {{1234}}`

- Использовать указанный http демон:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Запустить также веб-браузер:

`git instaweb --start --browser`

- Остановить текущий запущенный gitweb сервер:

`git instaweb --stop`

- Перезапустить текущий запущенный gitweb сервер:

`git instaweb --restart`
