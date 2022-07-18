# docker container

> Управление Docker контейнерами.

- Список запущенных Docker контейнеров:

`docker container ls`

- Запустить один или более остановленных контейнеров:

`docker container start {{container1_name}} {{container2_name}}`

- Убить (`kill -9`) один или более запущенных контейнеров:

`docker container kill {{container_name}}`

- Остановить несколько работающих контейнеров:

`docker container stop {{container_name}}`

- Поставить на паузу список указанных контейнеров:

`docker container pause {{container_name}}`

- Вывести детализированную информацию для указанных контейнеров:

`docker container inspect {{container_name}}`

- Экспортировать файловую систему контейнера в tar-архив:

`docker container export {{container_name}}`

- Создать докер-образ из изменений в контейнере:

`docker container commit {{container_name}}`
