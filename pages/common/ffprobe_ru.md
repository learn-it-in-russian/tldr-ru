# ffprobe

> Анализатор мультимедийного потока.

- Показывает все доступные потоки из медиафайла:

`ffprobe -v error -show_entries {{input.mp4}}`

- Отображает длительность медиафайла:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Отображает частоту кадров видео:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Показывает ширину или высоту видео:

`ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
