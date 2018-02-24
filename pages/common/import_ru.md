# import

> Захватывает экран X-сервера целиком или его часть и сохраняет полученное изображение в файл.
> Это часть библиотеки ImageMagick.

- Сохраняет экран целиком в формате PostScript:

`import -window root {{output.postscript}}`

- Сохраняет содержимое экрана удаленного X-сервера в формате PNG:

`import -window root -display {{remote_host}}:{screen}.{display} {{output.png}}`

- Сохраняет заданное по ID (отображается `xwininfo`) окно в формате JPEG:

`import -window {{window_id}} {{output.jpg}}`
