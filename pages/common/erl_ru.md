# erl

> Запускает и управляет программами на языке программирования Erlang.

- Собирает и запускает Erlang программу как обычный скрипт и выйти:

`erlc {{files}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- Присоединиться к запущенной Erlang ноде:

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- Загрузить модули Erlang из указанной директории:

`erl -pa {{directory_with_beam_files}}`
