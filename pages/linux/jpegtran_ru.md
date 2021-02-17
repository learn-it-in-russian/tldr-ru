# jpegtran

> Программа для преобразования JPEG файлов без потери качества.

- Отобразить изображение по горизонтали или вертикали:

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Повернуть изображение на 90, 180 или 270 градусов по часовой стрелке:

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Транспонировать (перевернуть) изображение по горизонтали (перевернуть по линии от лево-верх до право-низ):

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Транспонировать (перевернуть) изображение по горизонтали (право-верх - лево-низ):

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Конвертировать изображение в серый спектр:

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Вырезать из изображения прямоугольник ширины `W` и высоты `H` из верхнего-левого угла, сохранить результат в указанный файл:

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- Вырезать из изображения прямоугольник ширины `W` и высоты `H`, начиная с позиции `X` и `Y`. Сохранить результат в указанный файл:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`
