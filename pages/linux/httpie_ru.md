# httpie

> Удобная утилита для создания HTTP запросов из консоли.

- Отправить GET запрос (HTTP метод по умолчанию без дополнительных данных запроса):

`http {{https://example.com}}`

- Отправить POST запрос с параметрами:

`http {{https://example.com}} {{hello=World}}`

- Отправить POST запрос с данными, перенаправленными из файла:

`http {{https://example.com}} < {{file.json}}`

- Отправить PUT запрос с данными:

`http PUT {{https://example.com/todos/7}} {{hello=world}}`

- Послать DELETE запрос с заданным HTTP-заголовком:

`http DELETE {{https://example.com/todos/7}} {{API-Key:foo}}`

- Показать полную информацию об обменеданными между HTTP клиентом и сервером (запрос и ответ):

`http -v {{https://example.com}}`

- Загрузить файл:

`http --download {{https://example.com}}`
