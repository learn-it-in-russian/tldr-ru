# git switch

> Позволяет переключаться между ветками Git. Требует Git версии 2.23+.
> Смотри также [`git checkout`](https://900913.ru/tldr/common/ru/git-checkout/).

- Переключает на существующую ветку:

`git switch {{branch_name}}`

- Создаёт новую ветку и переключает на неё:

`git switch --create {{branch_name}}`

- Создать новую ветку, базируясь на существующем коммите и переключиться на неё:

`git switch --create {{branch_name}} {{commit}}`

- Переключиться на предыдущую ветку:

`git switch -`

- Переключиться на ветку м обновить все сабмодули:

`git switch --recurse-submodules {{branch_name}}`

- Переключиться на ветку и автоматически слить текущую ветку и все незакоммиченные изменения в неё:

`git switch --merge {{branch_name}}`
