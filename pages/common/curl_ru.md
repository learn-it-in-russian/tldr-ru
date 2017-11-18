# curl

> Передает или получает данные с сервера.
> Поддерживает множество протоколов, включая HTTP, FTP и POP3.

- Сохраняет содержимое по URL-адресу в файл:

`curl {{http://example.com}} -o {{filename}}`

- Скачивает файл, сохраняя его под названием из URL:

`curl -O {{http://example.com/filename}}`

- Скачивает файл, следуя перенаправлениям и автоматически продолжая докачку:

`curl -O -L -C - {{http://example.com/filename}}`

- Отправляет данные в виде формы (POST-запрос типа `application/x-www-form-urlencoded`):

`curl -d {{'name=bob'}} {{http://example.com/form}}`

- Отправляет запрос с дополнительным заголовком, используя заданный HTTP-метод:

`curl -H {{'X-My-Header: 123'}} -X {{PUT}} {{http://example.com}}`

- Отправляет данные в формате JSON, задав соответствующий тип содержимого в заголовке:

`curl -d {{'{"name":"bob"}'}} -H {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Передает имя пользователя и пароль для авторизации на сервере:

`curl -u myusername:mypassword {{http://example.com}}`

- Передает сертификат клиента и ключ к ресурсу, пропуская этап проверки сертификата:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
