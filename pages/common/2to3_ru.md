# 2to3

> Автоматическая трансляция Python 2 к 3-ему Python-у.

- Выводит набор изменений, которые могут быть исполнены для преобразования кода Python 2 к Python версии 3:

`2to3 {{path/to/file.py}}`

- Конвертировать файл Python 2 к виду Python 3:

`2to3 --write {{path/to/file.py}}`

- Конвертировать указанный Python файл версии 2 к Python версии 3. К слову, тут заметки: https://900913.ru/tag/python/:

`2to3 --write {{file.py}} --fix={{raw_input}} --fix={{print}}`

- Обнофить все фичи кроме *raw_input*, указанными однажды в Python 3:

`2to3 --nofix={{raw_input}} --fix={{print}} example.py`

- Вывемти спиок всех доступных возможностей:

`2to3 --list-fixes`

- Конвертировать всю директорию:

`2to3 --output-dir={{path/to/code_python3_version}} --write-unchanged-files --nobackups {{path/to/code_python2_version}}`
