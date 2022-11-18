# snowsql

> Клиент и интерфейс командной строки SnowSQL для облачного хранилища Snowflake.

- Подключиться к указанной базе данных <https://account.snowflakecomputing.com> (будет использован пароль из файла настроек, либо запрошен ввод пароля):

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- Присоединиться к базе данных, используя указанный файл конфигурации (по умолчанию `~/.snowsql/config`):

`snowsql --config {{path/to/configuration_file}}`

- Присоединиться к базе данных по умолчанию, используя токен для многофакторной аутентификации:

`snowsql --mfa-passcode {{token}}`

- Выполнить один SQL запрос или SnowSQL команду, используя соединение по умолчанию (полезно для скриптов командной оболочки):

`snowsql --query '{{query}}'`

- Выполнить команды из указанного файла, используя дефолтное соединение:

`snowsql --filename {{path/to/file.sql}}`
