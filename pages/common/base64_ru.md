# base64

> Закодировать или декодировать файл или стандартный поток ввода и вывести результат в стандартный поток вывода.

- Закодировать файл:

`base64 {{filename}}`

- Декодировать файл:

`base64 -d {{filename}}`

- Закодировать из стандартного потока ввода:

`{{somecommand}} | base64`

- Декодировать из стандартного потока ввода:

`{{somecommand}} | base64 -d`