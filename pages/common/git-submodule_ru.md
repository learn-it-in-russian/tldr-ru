# git submodule

> Проверяет, обновляет и управляет подмодулями.

- Установить указанные подмодули репозитория:

`git submodule update --init --recursive`

- Добавить репозиторий git в качестве подмодуля:

`git submodule add {{repository_url}}`

- Обновить каждый подмодуль до последней фиксации(коммита):

`git submodule foreach git pull`