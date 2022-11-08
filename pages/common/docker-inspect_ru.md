# docker inspect

> Программа для получения низкоуровневой информации о Docker объектах.

- Вывести справочную информацию:

`docker inspect`

- Вывести информацию о контейнере, образе или разделе по имени или ID:

`docker inspect {{container|image|ID}}`

- Получить IP-адрес контейнера:

`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{container}}`

- Выводит путь до файла журнала (лога) контейнера:

`docker inspect --format='{{.LogPath}}' {{container}}`

- Вывести имя образа контейнера:

`docker inspect --format='{{.Config.Image}}' {{container}}`

- Выводим конфигурационную информацию в формате JSON:

`docker inspect --format='{{json .Config}}' {{container}}`

- Вывести список всех подключённых портов:

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{container}}`
