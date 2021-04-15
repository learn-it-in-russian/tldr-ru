# getprop

> Вывести информацию о adb устройствах и эмуляторах.

- Вывести информацию о системных свойствах Android:

`getprop`

- Вывести информацию об указанных свойствах:

`getprop {{prop}}`

- Вывести уровень SDK API:

`getprop {{ro.build.version.sdk}}`

- Выводит версию Android:

`getprop {{ro.build.version.release}}`

- Напечатать модель Android устройства:

`getprop {{ro.vendor.product.model}}`

- Вывести статус OEM разблокировки:

`getprop {{ro.oem_unlock_supported}}`

- Выводит MAC адрес карты WiFi данного Android устройства:

`getprop {{ro.boot.wifimacaddr}}`
