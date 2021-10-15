# uvicorn

> ASGI Python HTTP сервер, для асинхронных проектов.

- Запустить веб-приложение Python:

`uvicorn {{import.path:app_object}}`

- Запустить вервер на порту 8080 на локальном хосте (localhost):

`uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}`

- Сключить "горячую перезагрузку" для отслеживания изменений:

`uvicorn --reload {{import.path:app_object}}`

- Использовать 4 рабочих процесса для обработки запросов:

`uvicorn --workers {{4}} {{import.path:app_object}}`

- Запустить приложение по HTTPS:

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}`
