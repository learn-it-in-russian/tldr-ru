# chcon

> Меняет контекст безопасности SELinux файла и директорий.

- Посмотреть контекст безопасности файла:

`ls -lZ {{path/to/file}}`

- Изменить контекст безопасности для указанного файла, используя контекст указанного файла:

`chcon --reference={{reference_file}} {{target_file}}`

- Изменить полностью контекст безовасности SELinux для указанного файла:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- Изменить только часть пользователя контекста безопасности SELinux:

`chcon -u {{user}} {{filename}}`

- Изменить только настройки роли контекста SELinux:

`chcon -r {{role}} {{filename}}`

- Аналогично, но только настройки типа контекста SELinux:

`chcon -t {{type}} {{filename}}`

- Изменить только контекст уровеня SELinux:

`chcon -l {{range/level}} {{filename}}`
