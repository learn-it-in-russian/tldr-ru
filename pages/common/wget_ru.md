# wget

> Загрузить файлы из веба.
> Поддерживает протоколы HTTP, HTTPS и FTP.

- Загрузить содержимое URL в файл:

`wget -O {{filename}} {{url}}`

- Ограничить скорость загрузки:

`wget --limit-rate={{200k}} {{url}}`

- Продолжить незаконченную загрузку:

`wget -c {{url}}`

- Сделать копию сайта в папке:

`wget --mirror -p --convert-links -P {{target_folder}} {{url}}`

- Загрузить с FTP с указанием имени и пароля пользователя:

`wget --ftp-user={{username}} --ftp-password={{password}} {{url}}`

- Повторять указанное количество раз загрузку, пока не получится:

`wget -t {{number_of_retries}} {{url}}`
