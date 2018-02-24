# dokku

> Мини-Heroku (PaaS) на базе Docker.
> Простое развертывание на сервере нескольких приложений на разных языках, используя единственную команду `git-push`.

- Список запущенных приложений:

`dokku apps`

- Создает приложение:

`dokku apps:create {{app_name}}`

- Удаляет приложение:

`dokku apps:destroy {{app_name}}`

- Устанавливает плагин:

`dokku plugin:install {{full_repo_url}}`

- Подключает базу данных к приложению:

`dokku {{db}}:link {{db_name}} {{app_name}}`
