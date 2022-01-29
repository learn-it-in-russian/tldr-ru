# pg_dumpall

> Получает sql файл или архив с сервера PostgreSQL.

- Выгрузить все базы данных в файл sql:

`pg_dumpall > {{path/to/file.sql}}`

- Получить все базы данных, доступные указанному пользователю. Сохранить их в файл sql:

`pg_dumpall --username={{username}} > {{path/to/file.sql}}`

- Также забекапить базы данных, сохранить в файл. Но в этот раз указываем адрес сервера и порт:

`pg_dumpall -h {{host}} -p {{port}} > {{output_file.sql}}`

- Получаем все базы данных, сохраняем их в специальный архивный формат со сжатием:

`pg_dumpall -Fc > {{output_file.dump}}`

- Dump only database data into an SQL-script file:

`pg_dumpall --data-only > {{path/to/file.sql}}`

- Выгрузить только схему базы данных в sql файл:

`pg_dumpall -s > {{output_file.sql}}`
