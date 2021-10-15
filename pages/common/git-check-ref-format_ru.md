# git check-ref-format

> Проверяет данный refname - допустимый ли, существует ли, проверяет статус.

- Проверяет формат указанной ссылки (refname):

`git check-ref-format {{refs/head/refname}}`

- Вывести имя последней проверенной ветки:

`git check-ref-format --branch @{-1}`

- Нормализовать refname:

`git check-ref-format --normalize {{refs/head/refname}}`
