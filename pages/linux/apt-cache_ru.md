# apt-cache

> Утилита для работы с кэшем пакетов в Debian и Ubuntu.

- Поиск (полнотекстовый) по всем доступным спискам пакетов:

`apt-cache search {{query}}`

- Отобразить информацию о пакете:

`apt-cache show {{package}}`

- Отобразить установлен ли пакет и обновлен ли он:

`apt-cache policy {{package}}`

- Отобразить все зависимости для пакета:

`apt-cache depends {{package}}`

- Отобразить пакеты, зависимые от данного пакета:

`apt-cache rdepends {{package}}`
