# choco-apikey

> Команда для управелния ключами API Chocolatey.

- Вывести список используемых репозиторев и их API ключи:

`choco apikey`

- Вывести указанный репозиторий с его ключём API:

`choco apikey --source "{{source_url}}"`

- Установить API ключ для репозитория:

`choco apikey --source "{{source_url}}" --key "{{api_key}}"`

- Удалить API ключ для репозитория:

`choco apikey --source "{{source_url}}" --remove`
