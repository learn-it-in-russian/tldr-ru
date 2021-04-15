# settings

> Получает информацию об операционной системе Android.

- Вывести список настроек пространства имён `global`:

`settings list {{global}}`

- Выводит значения указанных настроек:

`settings get {{global}} {{airplane_mode_on}}`

- Устанавливает значение указанной настройки:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Удаляет указанную настройку:

`settings delete {{secure}} {{screensaver_enabled}}`
