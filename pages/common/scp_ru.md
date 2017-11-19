# scp

> Защищенное копирование.
> Копирует файлы между хостами с использованием Secure Copy Protocol поверх SSH.

- Копирует локальный файл на удаленную машину:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Копирует файл с удаленной машины в локальный каталог:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_dir}}`

- Рекурсивно копирует содержимое каталога на удаленной машине в локальный каталог:

`scp -r {{remote_host}}:{{path/to/remote_dir}} {{path/to/local_dir}}`

- Копирует файл между двумя удаленными хостами через локальный хост:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_dir}}`

- Использует заданное имя пользователя при подключении к удаленному хосту:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_dir}}`

- Использует заданный SSH-ключ для авторизации на удаленной машине:

`scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}`
