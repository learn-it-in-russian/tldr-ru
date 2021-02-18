# git bundle

> Упаковать объекты и ссылки (refs) в архив.

- Создать файл пакета, который содержит все объекты и ссылки указанной ветки:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Создать файл пакета для всех веток репозитория:

`git bundle create {{path/to/file.bundle}} --all`

- Создать бандл-файл для последних 5 коммитов текущей ветки:

`git bundle create {{path/to/file.bundle}} -{{5}} {{HEAD}}`

- Создать бандл для объектов за последние 7 дней:

`git bundle create {{path/to/file.bundle}} --since={{7.days}} {{HEAD}}`

- Проверяет на правильность данный бандл. Также проверяет, может ли он быть применён к текущему репозиторию:

`git bundle verify {{path/to/file.bundle}}`

- Вывести на стандартный поток вывода список всех ссылок, содержащихся в данном бандле:

`git bundle unbundle {{path/to/file.bundle}}`

- Распаковать указанную ветку из бандла в текущий репозиторий:

`git pull {{path/to/file.bundle}} {{branch_name}}`
