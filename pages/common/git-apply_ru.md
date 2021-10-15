# git apply

> Применить патч к файлу или к индексу.

- Выводить сообщения о пропатченных файлах:

`git apply --verbose {{path/to/file}}`

- Применить и добавить пропатченные файлы к индексу:

`git apply --index {{path/to/file}}`

- Применить патч-файл с веб-сайта:

`curl {{https://example.com/file.patch}} | git apply`

- Вывести информацию (diffstat) для ввода и применить патч:

`git apply --stat --apply {{path/to/file}}`

- Применить патч в обратном порядке:

`git apply --reverse {{path/to/file}}`

- Сохранить результаты применения патча в индексе без изменения самих файлов:

`git apply --cache {{path/to/file}}`
