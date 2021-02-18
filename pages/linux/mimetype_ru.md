# mimetype

> Автоматически определяет MIME-тип файла.
- Вывести MIME-тип указанного файла:

`mimetype {{path/to/file}}`

- Вывести только MIME-тип, без имени файла:

`mimetype --brief {{path/to/file}}`

- Вывести описание MIME типа для указанного файла:

`mimetype --describe {{path/to/file}}`

- Определить MIME тип для данных, переданных через входной поток (stdin):

`{{some_command}} | mimetype --stdin`

- Вывести отладочную информацию о процессе определения MIME типа:

`mimetype --debug {{path/to/file}}`

- Вывести все возможные MIME типы указанного файла в порядке точности:

`mimetype --all {{path/to/file}}`

- Указать 2 буквы языка для вывода информации:

`mimetype --language={{ru}} {{path/to/file}}`

