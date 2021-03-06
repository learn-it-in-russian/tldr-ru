# git bisect

> Методом двоичного поиска ищет коммит, в котором появилась ошибка.
> Git автоматически прыгает по графу коммитов, постепенно сужая область поиска до одного коммита.

- Начитает поиск в диапазоне коммитов, ограниченном коммитом с ошибкой и известным коммитом без ошибки:

`git bisect start {{bad_commit}} {{good_commit}}`

- После тестирования помечайте коммит как "плохой" (bad) или "хороший" (good):

`git bisect {{good|bad}}`

- После того, как `git bisect` найдет коммит с ошибкой, завершите сеанс bisect и вернитесь на предыдушую ветку:

`git bisect reset`

- Пропустить коммит (например, когда тестирование не проходит из-за другой проблемы):

`git bisect skip`
