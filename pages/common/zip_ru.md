# zip

> Упаковка и сжатие (архивирование) файлов в zip-файл.

- Упаковка и сжатие каталога и его содержимого, рекурсивно:

`zip -r {{compressed.zip}} {{/path/to/dir}}`

- Исключение нежелательных файлов из добавления в сжатый архив:

`zip -r {{compressed.zip}} {{path/to/dir}} -x \*.git\* \*node_modules\* ...`

- Архивирование каталога и его содержимого с самым высоким уровнем сжатия [9]:

`zip -r -{{9}} {{compressed.zip}} {{/path/to/dir}}`

- Упаковка и сжатие нескольких каталогов и файлов:

`zip -r {{compressed.zip}} {{/path/to/dir1 /path/to/dir2 /path/to/file}}`

- Добавление файлов в существующий zip-файл:

`zip {{compressed.zip}} {{path/to/file}}`

- Удаление файлов из существующего zip-файла:

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`
