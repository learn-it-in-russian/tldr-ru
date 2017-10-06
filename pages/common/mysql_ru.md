# mysql

> Инструменты командной строки MySQL.

- Присоединиться к базе данных:

`mysql {{database_name}}`

- Присоединиться к базе данных указанным пользователем, ввести пароль интерактивно:

`mysql -u {{user}} --password {{database_name}}`

- Присоединиться к базе данных на другом хосте:

`mysql -h {{database_host}} {{database_name}}`

- Выполнить SQL запросы из файла:

`mysql {{database_name}} < {{script.sql}}`
