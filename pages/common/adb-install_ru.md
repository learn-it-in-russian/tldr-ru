# adb install

> Установщик для моста Android Debug: посылает пакеты на Android эмулятор или подсоединённому Android устройству.

- Залить приложение Android на эмуляторе или девайсе:

`adb install {{path/to/file.apk}}`

- Переустановить существующее приложение, сохраняя его данные:

`adb install -r {{path/to/file.apk}}`

- Получить все права доступа, выведенные в манифесте приложения:

`adb install -g {{path/to/file.apk}}`

- Быстро обновить установленные пакеты, только если они изменены в APK:

`adb install --fastdeploy {{path/to/file.apk}}`
