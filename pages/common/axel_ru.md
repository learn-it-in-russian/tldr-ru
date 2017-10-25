# axel

> Ускоритель скачивания.
> Поддерживает HTTP, HTTPS и FTP.

- Скачать URL в файл:

`axel {{url}}`

- Скачать URL и указать имя файла:

`axel {{url}} -o {{filename}}`

- Скачать с несколькими подключениями:

`axel -n {{connections_num}} {{url}}`

- Поиск зеркал:

`axel -S {{mirror_num}} {{url}}`

- Ограничить скорость скачивания (байт в секунду):

`axel -s {{speed}} {{url}}`