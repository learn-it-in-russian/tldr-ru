# abbr

> Управляет аббревиатурами в оболочке [`fish`](https://900913.ru/tldr/common/en/fish/).
> Сокращения, определённые пользователем, которые вставляются в месте использования, подменяясь более длинными фразами команд.

- Добавить сокращение (алиас):

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- Переименовать существующее сокращение:

`abbr --rename {{old_name}} {{new_name}}`

- Удалить существующий алиас оболоски исполнения команд:

`abbr --erase {{abbreviation_name}}`

- Получить алиасы с другого хоста по SSH:

`ssh {{host_name}} abbr --show | source`
