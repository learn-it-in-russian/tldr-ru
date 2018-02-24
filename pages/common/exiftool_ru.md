# exiftool

> Читает и пишет метаданные в файлы.

- Удаляет все EXIF-метаданные из заданных файлов:

`exiftool -All= {{file}}`

- Во всех фотографиях в папке сдвигает время съемки на 1 час вперед:

`exiftool "-AllDates+=0:0:0 1:0:0" {{directory}}`

- Во всех JPEG-файлах сдвигает время съемки на 1 день и 1 час назад:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Изменяет DateTimeOriginal на -1.5 часа, не делая резервных копий:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Переименовывает всех файлы JPEG в соответствии с DateTimeOriginal:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{directory}} -r -ext jpg`
