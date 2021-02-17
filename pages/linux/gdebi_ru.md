# gdebi

> Простая утилита для установки программ из `.deb` файлов.

- Установить локально `.deb` пакет и разрешить + установить зависимости:

`gdebi {{path/to/package.deb}}`

- Вывести версию программы:

`gdebi --version`

- Не показывать прогресс установки ("тихий режим"):

`gdebi {{path/to/package.deb}} --quiet`

- Установить конфигурационные опции APT:

`gdebi {{path/to/package.deb}} --option={{APT_OPTS}}`

- Использовать альтернативную корневую директорию:

`gdebi {{path/to/package.deb}} --root={{path/to/root_dir}}`
