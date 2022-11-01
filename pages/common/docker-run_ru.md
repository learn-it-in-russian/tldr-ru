# docker run

> Запускает команду в новом Docker контейнере.

- Запустить команду в новом контейнере из отмеченного образа:

`docker run {{image:tag}} {{command}}`

- Запустить команду в новом контейнере в фоне (выводится идентификатор контейнера)Run command in a new container in background and display its ID:

`docker run --detach {{image}} {{command}}`

- Запускает команду в "одноразовом" контейнере в интерактивном режиме псевдо-терминала:

`docker run --rm --interactive --tty {{image}} {{command}}`

- Запустить команду в новом контейнере и передать туда переменные окружения:

`docker run --env '{{variable}}={{value}}' --env {{variable}} {{image}} {{command}}`

- Запустить команду в новом контейнере с примонтированным разделом (папкой) из файловой системы хостовой машины:

`docker run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image}} {{command}}`

- Запустить команду в новом контейнере, прокинув наружу сетевой порт:

`docker run --publish {{host_port}}:{{container_port}} {{image}} {{command}}`

- Запустить команду в новом контейнере, изменив точку входа образа:

`docker run --entrypoint {{command}} {{image}}`

- Запустить команду в новом контейнере и присоединить к существующей docker сети:

`docker run --network {{network}} {{image}}`
