# redis-cli

> Создать соединение с Radis сервером.

- Подключиться к локальному серверу:

`redis-cli`

- Подключиться к удалённому серверу через порт по умолчанию (6379):

`redis-cli -h {{host}}`

- Подключиться к удалённому серверу, указав номер порта:

`redis-cli -h {{host}} -p {{port}}`

- Указать пароль:

`redis-cli -a {{password}}`

- Выполнить Redis команду:

`redis-cli {{redis_command}}`