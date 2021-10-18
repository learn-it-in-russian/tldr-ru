# a2dissite

> Отключить виртуальный хост Apache в операционных системах на базе Debian.
> More information: <https://manpages.debian.org/latest/apache2/a2dissite.8.en.html>.

- Отключить виртуальный хост:

`sudo a2dissite {{virtual_host}}`

- Не показывать информационные сообщения:

`sudo a2dissite --quiet {{virtual_host}}`
