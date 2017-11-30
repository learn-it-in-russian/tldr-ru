# cabal

> Консольный интерфейс к пакетной инфраструктуре Haskell (Cabal).
> Управляет проектами Haskell и пакетами Cabal из репозитория пакетов Hackage.

- Выводит список пакетов из Hackage:

`cabal list {{search_string}}`

- Показывает сведения о пакете:

`cabal info {{package_name}}`

- Скачивает и устанавливает пакет:

`cabal install {{package_name}}`

- Создает в текущей папке новый проект Haskell:

`cabal init`

- Проводит сборку проекта в текущей папке:

`cabal build`

- Запускает тесты проекта в текущей папке:

`cabal test`
