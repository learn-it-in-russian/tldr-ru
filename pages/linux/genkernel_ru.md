# genkernel

> Утилита Gentoo Linux для компиляции и установки ядер.

- Автоматически скомпилировать и установить стандартное ядро:

`sudo genkernel all`

- Создать и установить только bzImage|initramfs|kernel|ramdisk:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- Применить изменения к конфигурации ядра перед компиляцией и установкой:

`sudo genkernel --menuconfig all`

- Создать ядро с пользовательским именем:

`sudo genkernel --kernname={{пользовательское_имя}} all`

- Использовать источник ядра вне директории по умолчанию /usr/src/linux:

`sudo genkernel --kerneldir={{путь/к/директории}} all`
