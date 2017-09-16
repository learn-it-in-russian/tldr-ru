# docker

> Управление Docker контейнерами и образами.

- Список работающих docker контейнеров:

`docker ps`

- Список всех docker контейнеров (работающих и остановленных):

`docker ps -a`

- Запуск контейнера:

`docker start {{container}}`

- Остановка контейнера:

`docker stop {{container}}`

- Запуск контейнера из образа и получение командной оболочки внутри:

`docker run -it {{image}} bash`

- Исполнение команды внутри работающего контейнера:

`docker exec {{container}} {{command}}`

- Удаление контейнера:

`docker rm {{container}}`
