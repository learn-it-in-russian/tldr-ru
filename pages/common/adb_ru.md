# adb

> Android Debug Bridge: связь с эмулятором Android или подключенными устройствами Android.

- Проверка, запущен ли процесс сервера adb и запуск его:

`adb start-server`

- Завершить процесс сервера adb:

`adb kill-server`

- Запуск удаленной командной оболочки на эмуляторе/устройстве:

`adb shell`

- Отправить Android-приложение на эмулятор/устройство:

`adb install -r {{path/to/file.apk}}`

- Скопировать файл или дирректорию с устройства:

`adb pull {{path/to/device_file_or_folder}} {{path/to/local_destination_folder}}`

- Скопировать файл или дирректорию на устройство:

`adb push {{path/to/local_file_or_folder}} {{path/to/device_destination_folder}}`

- Получить список подключённых устройств:

`adb devices`
