# docker login

> Команда для входа на сервер хранилища образов docker.

- Интерактивный интерфейс для входа на сервер docker образов:

`docker login`

- Войти на сервер образов под указанным именем (будет запрошен пароль):

`docker login --username {{username}}`

- Войти на указанный сервер под определённым пользователем с указанным паролем:

`docker login --username {{username}} --password {{password}} {{server}}`

- Войти на сервер, передав пароль на stdin:

`echo "{{password}}" | docker login --username {{username}} --password-stdin`
