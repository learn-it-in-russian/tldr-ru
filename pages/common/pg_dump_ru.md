# pg_dump

> Извлекает из PostgreSQL базы данных в скрипт-файл или в архив.

- Сохраняет базу данных в SQL-скрипт файл:

`pg_dump {{db_name}} > {{output_file.sql}}`

- То же, что и предыдущее, но указываем пользователя:

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- То же, что и предыдущее, но указываем хост и порт:

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- Сохраняет базу данных в специальный файл архива:

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`

- Сохраняет только данные базы данных в файл скрипта SQL:

`pg_dump -a {{db_name}} > {{path/to/output_file.sql}}`

- Сохраняет только схему (определение структур таблиц) базы данных в файл скрипта SQL:

`pg_dump -s {{db_name}} > {{path/to/output_file.sql}}`
