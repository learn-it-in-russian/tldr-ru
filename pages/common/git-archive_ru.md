# git archive

> Создать архив файлов из рабочего дерева.

- Создать *tar* архив из содержимого текущего HEAD (последнего коммита проекта) и вывести его на стандартный вывод (stdout):

`git archive --verbose HEAD`

- Создать *zip* архив для текущего последнего состояния проекта и вывести на стандартный поток вывода (stdout):

`git archive --verbose --format=zip HEAD`

- То же самое, что и предыдущая команда, но указываем результирующий файл для *zip* архива:

`git archive --verbose --output={{path/to/file.zip}} HEAD`

- Создать *tar* архив из содержимого последнего коммита указанной ветки:

`git archive --output={{path/to/file.tar}} {{branch_name}}`

- Создать *tar* архив из файлов указанной директории (из HEAD) и вывести в указанный файл:

`git archive --output={{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Приписать путь перед путём каждого файла для записи в архив. Архивируем указанную директорию из HEAD:

`git archive --output={{path/to/file.tar}} --prefix={{path/to/prepend}}/ HEAD`
