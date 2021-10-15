# Medusa

> Модульный и параллельный брутфорсер (переборщик) данных для входа в систему для различных протоколов.

- Запустить брутфорс (перебор) входных данных для FTP сервера, используя файл базы данных с именами пользователей и файл с паролями (перебор по словарю):

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- Попытаться войти на HTTP сервер, используя указанные имя пользователя, пароль и user-agent:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Запустить брутфорс входных данных для MySQL сервера, используя файлы: имён пользователей и хэшей:

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- Запустить брутфорс входных данных для списка SMB серверов, используя имя пользователя и pwdump файл:

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
