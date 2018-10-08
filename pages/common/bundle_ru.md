# bundle

> Менеджер зависимостей для языка программирования Ruby.

- Устанавливает все gem-пакеты, определенные в файле `gemfile`, ожидаемом в рабочем каталоге:

`bundle install`

- Обновляет все gem-пакеты по правилам, определенным в gemfile и пересоздаёт gemfile.lock:

`bundle update`

- Обновляет один gem-пакет, определенный в gemfile:

`bundle update --source {{gemname}}`

- Создаёт новый шаблон gem-пакета:

`bundle gem {{gemname}}`
