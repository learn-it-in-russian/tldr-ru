# base32

> Закодировать или декодировать файл или стандартный поток ввода и вывести результат в стандартный поток вывода.

- Закодировать файл:

`base32 {{filename}}`

- Декодировать файл:

`base32 -d {{filename}}`

- Закодировать из стандартного потока ввода:

`{{somecommand}} | base32`

- Декодировать из стандартного потока ввода:

`{{somecommand}} | base32 -d`