# pg_restore

> Восстанавливает базу данных PostgreSQL из файла архива, созданного командой `pg_dump`.

- Восстановить из архива в существующую базу данных:

`pg_restore -d {{db_name}} {{archive_file.dump}}`

- То же, что и предыдущее, но указываем пользователя:

`pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}`

- То же, что и предыдущее, но указываем хост и порт:

`pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}`

- Вывести список баз данных, содержащихся в архиве:

`pg_restore --list {{archive_file.dump}}`

- Очистить базы данных перед созданием их:

`pg_restore --clean -d {{db_name}} {{archive_file.dump}}`

- Запустить восстановление в параллельно в 2 задачи:

`pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}`
