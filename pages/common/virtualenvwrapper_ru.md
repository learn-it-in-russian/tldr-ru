# virtualenvwrapper

> Набор простых программ, основанных на `virtualenv`, для управления виртуальных изолированных окружений Python. Обёртка над `virtualenv`.

- Создать новое окружение Python `virtualenv` в домашней директории пользователя (`$WORKON_HOME`):

`mkvirtualenv {{virtualenv_name}}`

- Создать `virtualenv` с указанной версией Python:

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- Активировать и использовать другое окружение `virtualenv`:

`workon {{virtualenv_name}}`

- Перестать использовать текущий `virtualenv`:

`deactivate`

- Список всех готовых к использованию окружений:

`lsvirtualenv`

- Удалить указанный `virtualenv`:

`rmvirtualenv {{virtualenv_name}}`

- Получить общую информацию о всех командах `virtualenvwrapper`:

`virtualenvwrapper`
