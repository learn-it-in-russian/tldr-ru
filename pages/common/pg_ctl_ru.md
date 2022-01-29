# pg_ctl

> Утилита для управления сервером PostgreSQL, кластером баз данных.

- Инициализировать новый PostgreSQL сервер:

`pg_ctl -D {{data_directory}} init`

- Запустить сервер PostgreSQL:

`pg_ctl -D {{data_directory}} start`

- Остановить PostgreSQL сервер:

`pg_ctl -D {{data_directory}} stop`

- Перезапустить PostgreSQL сервер:

`pg_ctl -D {{data_directory}} restart`

- Перечитать и применить конфигурацию PostgreSQL сервера:

`pg_ctl -D {{data_directory}} reload`
