# shasum

> Вычисляет или проверяет криптографическую сумму SHA.

- Вычислить SHA1 чек-сумму для файла:

`shasum {{path/to/file}}`

- Вычислить SHA256 чек-сумму для файла:

`shasum --algorithm 256 {{path/to/file}}`

- Вычислить SHA512 чек-сумму для нескольких файлов:

`shasum --algorithm 512 {{path/to/file1}} {{path/to/file2}}`

- Посчитать SHA256 чек-суммы и сохранить список в файл:

`shasum --algorithm 256 {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}`

- Проверить файл со списком чек-сумм для файлов директории:

`shasum --check {{path/to/file}}`

- Проверяет список сумм и выводит сообщение только, если проверка файла провалилась:

`shasum --check --quiet {{path/to/file}}`

- Вычисляет SHA1 чексумму со стандартного потока ввода (stdin):

`{{some_command}} | shasum`
