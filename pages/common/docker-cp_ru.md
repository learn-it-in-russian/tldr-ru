# docker cp

> Копирует файлы и директории между хостовой и контейнерной файловыми системами.

- Скопировать файл или директорию с хоста в контейнер:

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Скопировать файл или директорию из контейнера на хостовую файловую систему:

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Скопировать файл или директорию с хоста в контейнер, следуя символьным ссылкам (копирует симлинки как файлы, на которые указывает, а не просто ссылки неизветно куда):

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
