# oc

> Контейнер OpenShift для консольного интерфейса Platform CLI.
> Позволяет использовать менеджер контейнеров.

- Войти в OpenShift контейнер Platform сервера:

`oc login`

- Создать новый проект:

`oc new-project {{project_name}}`

- Перейти в существующий проект:

`oc project {{project_name}}`

- Добавить новое приложение в проект:

`oc new-app {{repo_url}} --name {{application}}`

- Открыть удалённый консольный интерфейс в контейнере:

`oc rsh {{pod_name}}`

- Выводит список задач проекта:

`oc get pods`

- Выйти из текущеё сессии:

`oc logout`
