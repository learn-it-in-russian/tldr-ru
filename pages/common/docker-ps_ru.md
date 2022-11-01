# docker ps

> Выводит список Docker контейнеров.

- Список запущенных контейнеров:

`docker ps`

- Выводит список всех docker контейнеров (запущенных и остановленных):

`docker ps --all`

- Показывает последний запущенный контейнер (не зависит от состояния контейнера):

`docker ps --latest`

- Выводит список контейнеров, отфильтрованный по имени (ищется подстрока):

`docker ps --filter="name={{name}}"`

- Выводит контейнеры, образы которых наследуются от указанного образа:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Фильтрует список контейнеров по коду возврата:

`docker ps --all --filter="exited={{code}}"`

- Отфильтровать список контейнеров по статусу (created, running, removing, paused, exited и dead):

`docker ps --filter="status={{status}}"`

- Отфильтровать список контейнеров и оставить только те, кто примонтировал указанную директорию:

`docker ps --filter="volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
