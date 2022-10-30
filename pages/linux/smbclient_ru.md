# smbclient

> FTP-подобный клиент для доступа к ресурсам на серверах SMB/CIFS.

- Присоединиться к ресурсу `//server/share`
  (у пользователя запросят пароль; для выхода из сессии используется команда `exit`):

`smbclient {{//server/share}}`

- Присоединиться к ресурсу под другим именем:

`smbclient {{//server/share}} --user {{username}}`

- Присоединиться, используя другую рабочую группу:

`smbclient {{//server/share}} --workgroup {{domain}} --user {{username}}`

- Открыть соединение, указав пользователя и пароль:

`smbclient {{//server/share}} --user {{username%password}}`

- Скачать файл с сервера:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "get {{file.txt}}"`

- Загрузить файл на сервер:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "put {{file.txt}}"`

- Вывести список доступных ресурсов на сервере анонимно:

`smbclient --list={{server}} --no-pass`
