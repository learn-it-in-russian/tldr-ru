# docker login

> Войти (залогиниться) в docker registry (хранилище образов).

- Интерактивный вход в регистри:

`docker login`

- Войти в регистри с указанным именем пользователя (потребует ввода пароля):

`docker login --username {{username}}`

- При входе указываем из команды имя пользователя, пароль и хост:

`docker login --username {{username}} --password {{password}} {{server}}`

- Логинимся в регистри, указывая имя пользователя, а пароль передаём на стандартный поток ввода (stdin):

`echo "{{password}}" | docker login --username {{username}} --password-stdin`
