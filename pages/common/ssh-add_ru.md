# ssh-add

> Управляет загруженными ssh ключами в [ssh-agent](https://900913.ru/tldr/common/ru/ssh-agent/).
> Убедитесь, что ssh-agent запущен, чтобы ключи могли быть загруженными в него.
> More information: <https://man.openbsd.org/ssh-add>.

- Добавить ssh ключи из директории по умолчанию (`~/.ssh`) в ssh-agent:

`ssh-add`

- Добавить указанный ключ в ssh-agent:

`ssh-add {{path/to/private_key}}`

- Вывести список "отпечатков" загруженных ключей:

`ssh-add -l`

- Удалить ключ из ssh-agent-а:

`ssh-add -d {{path/to/private_key}}`

- Удалить все загруженные ключи ssh-agent-а:

`ssh-add -D`

- Добавляет ключ с его цепочкой ключей в ssh-agent:

`ssh-add -K {{path/to/private_key}}`
