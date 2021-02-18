# gitlab-ctl

> Консольная утилита для управления GitLab.

- Вывести статус каждого сервиса:

`sudo gitlab-ctl status`

- Выводит состояние указанного сервиса:

`sudo gitlab-ctl status {{nginx}}`

- Перезапустить все сервисы:

`sudo gitlab-ctl restart`

- Перезапустить указанный сервис:

`sudo gitlab-ctl restart {{nginx}}`

- Вывести журнал (лог) для всех сервисов и продолжать выводить, пока не нажата комбинация `Ctrl + C`:

`sudo gitlab-ctl tail`

- Вывести журнал (лог) для указанного сервиса:

`sudo gitlab-ctl tail {{nginx}}`
