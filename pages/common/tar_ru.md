# tar

> Утилита архивации.
> Часто совмещается со сжатием, таким как gzip или bzip.

- Создает архив из файлов:

`tar cf {{target.tar}} {{file1 file2 file3}}`

- Создает сжатый gzip архив:

`tar czf {{target.tar.gz}} {{file1 file2 file3}}`

- Извлекает архив в заданную папку:

`tar xf {{source.tar}} -C {{folder}}`

- Извлекает сжатый gzip архив в текущий каталог:

`tar xzf {{source.tar.gz}}`

- Извлекает сжатый bzip архив в текущий каталог:

`tar xjf {{source.tar.bz2}}`

- Создает сжатый архив, определяя метод сжатия по расширению:

`tar caf {{target.tar.xz}} {{file1 file2 file3}}`

- Выводит список содержимого tar-файла:

`tar tvf {{source.tar}}`
