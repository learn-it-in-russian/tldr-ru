# convmv

> Изменение кодировки имени файла (НЕ содержимого файла) из одной в другую.

- Проверка изменения кодировки имени(ничего не изменяет на самом деле):

`convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Изменение кодировки имени файла:

`convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}`
