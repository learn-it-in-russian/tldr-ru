# apt-key

> Утилита управления ключами репозиториев пакетного менеджера APT в Debian и Ubuntu.

- Отобразить список доверенных ключей:

`apt-key list`

- Добавить ключ в список доверенных:

`apt-key add {{public_key_file.asc}}`

- Удалить ключ из списка доверенных:

`apt-key del {{key_id}}`

- Добавить удаленный ключ (по ссылке) в список доверенных:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Добавить ключ с сервера ключей для определенного ключа:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
