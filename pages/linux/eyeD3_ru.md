# eyeD3

> Работа с метаданными в MP3 файлах.

- Отобразить информацию о MP3 файле:

`eyeD3 {{filename.mp3}}`

- Задать название композиции в MP3 файле:

`eyeD3 --title {{"A Title"}} {{filename.mp3}}`

- Задать название альбома всем MP3 файлам в директории:

`eyeD3 --album {{"Album Name"}} {{*.mp3}}`

- Задать файл обложки MP3 файла:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
