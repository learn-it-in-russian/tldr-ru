# ffmpeg

> Утилита конвертации видео.

- Извлечь звуковую дорожку из видео и сохранить ее в MP3:

`ffmpeg -i {{video_filename}} -vn -ar 44100 -ac 2 -ab 192 -f mp3 {{sound.mp3}}`

- Извлечь кадры из видео или GIF в отдельные пронумерованные изображения:

`ffmpeg -i {{video_or_gif_filename}} {{image%d.png}}`

- Склеить отдельные изображения (image1.jpg, image2.jpg, и т.д.) в видео-файл или GIF:

`ffmpeg -f image2 -i {{image%d.jpg}} {{video.mpg_or_video.gif}}`

- Конвертировать  AVI файл в MP4. Параметры: AAC Audio @ 128kbit, Video @ 1250Kbit:

`ffmpeg -i {{in.avi}} -acodec libfaac -ab 128k -vcodec mpeg4 -b 1250K {{out.mp4}}`
