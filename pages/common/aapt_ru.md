# aapt

> Приложение упаковки ресурсных файлов для Андроид (Android Asset Packaging Tool).
> Собирает и упаковывает ресурсы приложения Android.

- Выводит список файлов, содержащихся в APK архиве:

`aapt list {{path/to/app.apk}}`

- Показывает метаданные приложения (версия, требуемые права доступа и т.д.):

`aapt dump badging {{path/to/app.apk}}`

- Создаёт новый APK архив с файлами из указанной директории:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
