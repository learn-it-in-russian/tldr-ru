# gitlab-runner

> Консольная утилита для управления раннерами (хостами для запуска тестов) GitLab.

- Зарегистрировать новый раннер:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- Зарегистрировать раннер, запускаемый в Docker-е:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- Отменить регистрацию раннера:

`sudo gitlab-runner unregister --name {{name}}`

- Показать состояние запущенного сервиса:

`sudo gitlab-runner status`

- Перезапустить `gitlab-runner`:

`sudo gitlab-runner restart`

- Проверить, могут ли зарегистрированные раннеры присоединиться к GitLab:

`sudo gitlab-runner verify`
