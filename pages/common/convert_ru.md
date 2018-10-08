# convert

> Конвертация изображений при помощи Imagemagick .

- Конвертировать изображение из JPG в PNG:

`convert {{image.jpg}} {{image.png}}`

- Маштабировать изображение в 50% от оригинальнго размера:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Машбатировать изображение сохраняя пропорции сторон к максимальному разрешению 640x480:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Горизонтально склеить изображения:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`
