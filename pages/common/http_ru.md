# http

> HTTPie: HTTP-клиент, дружелюбная замена cURL.

- Загружает URL в файл:

`http -d {{example.org}}`

- Отправляет форму:

`http -f {{example.org}} {{name='Борис'}} {{profile_picture@'bob.png'}}`

- Отправляет объект JSON:

`http {{example.org}} {{name='Борис'}}`

- Задает метод HTTP:

`http {{HEAD}} {{example.org}}`

- Добавляет дополнительный заголовок:

`http {{example.org}} {{X-MyHeader:123}}`

- Отправляет имя пользователя и пароль для авторизации на сервере:

`http -a {{username:password}} {{example.org}}`

- Формирует тело запроса из стандартного ввода:

`cat {{data.txt}} | http PUT {{example.org}}`
