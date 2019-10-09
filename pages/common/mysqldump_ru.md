# mysqldump

> Создает резервные копии баз данных MySQL.

- Создать резервную копию, с требованием ввода пароля пользователя:

`mysqldump -u {{user}} --password {{database_name}} > {{filename.sql}}`

- Восстановить резервную копию, с требованием ввода пароля пользователя:

`mysql -u {{user}} --password {{database_name}} < {{filename.sql}}`
