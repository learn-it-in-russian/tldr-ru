# rclone

> Консольная программа для копирования/синхронизации/перемещения файлов и папок на/между облачными сервисами.

- Список содержимого директории на rclone удалённом сервере:

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- Копирует файл или директорию с локального диска на удалённый сервер:

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/destination_directory}}`

- Копируем с удалённого источника в локальную директорию:

`rclone copy {{remote_name}}:{{path/to/source_file_or_directory}} {{path/to/destination_directory}}`

- Синхронизируем локальную директорию с удалённой. Изменяет только папку назначения:

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Перемещает файл или директорию с локальгого диска на удалённый сервер:

`rclone move {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Удаляет файл или директорию с удалённого сервера (с ключом `--dry-run` только выведет список для удаления, но изменений не внесёт):

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}`

- Монтирует к файловой системе удалённый ресурс rclone (экспериментальная возможность):

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- Отмонтировать удалённый ресурс rclone от файловой системы, если CTRL-C не помогает:

`fusermount -u {{path/to/mount_point}}`
