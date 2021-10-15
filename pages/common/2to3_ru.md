# 2to3

> Автоматически преобразовывает код Python 2 к версии 3.

- Выводит изменения, которые могут быть применены без их исполнения (dry-run):

`2to3 {{path/to/file.py}}`

- Преобразовать код указанного файла Python 2 к коду Python 3:

`2to3 --write {{path/to/file.py}}`

- Совержить преобразование указанных возможностей языка Python 2 к Python 3:

`2to3 --write {{path/to/file.py}} --fix={{raw_input}} --fix={{print}}`

- Совершить преобразование, исключив указанные возможности (функции / команды языка):

`2to3 --write {{path/to/file.py}} --nofix={{has_key}} --nofix={{isinstance}}`

- Выводит список всех возможных преобразований, которые могут быть исполнены при преобразовании Python 2 к Python 3:

`2to3 --list-fixes`

- Сконвертировать все Python 2 файлы директории к Python 3:

`2to3 --output-dir={{path/to/python3_directory}} --write-unchanged-files --nobackups {{path/to/python2_directory}}`

- Запустить 2to3 в несколько потоков:

`2to3 --processes={{4}} --output-dir={{path/to/python3_directory}} --write --nobackups --no-diff {{path/to/python2_directory}}`
