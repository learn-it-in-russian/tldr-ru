# git restore

> Восстанавливает рабочее дерево файлов. Работает в Git с версии 2.23+.
> 
> Смотри также [git checkout](https://900913.ru/tldr/common/ru/git-checkout/)
> и [git reset](https://900913.ru/tldr/common/ru/git-reset/).

- Восстановить и вернуть файл к версии, соответствующей текущему коммиту (HEAD):

`git restore {{path/to/file}}`

- Восстановить и вернуть файл к версии коммита, указанного в параметере `{{commit}}`:

`git restore --source {{commit}} {{path/to/file}}`

- Отменить все незафиксированные изменения во всех отслеживаемых файлах:

`git restore :/`

- Убрать файл из коммита:

`git restore --staged {{path/to/file}}`

- Убрать все файлы из коммита:

`git restore --staged :/`

- Отменить все изменения в файлах (в добавленных в коммит и не добавленных):

`git restore --worktree --staged :/`

- Интерактивный интерфейс для выбора файлов для восстановления:

`git restore --patch`
