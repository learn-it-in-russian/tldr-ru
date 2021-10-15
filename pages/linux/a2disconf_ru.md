# a2disconf

> Отключить файл конфигурации Apache в операционных системах на базе Debian.
> Для большей информации смотрите: <https://manpages.debian.org/latest/apache2/a2disconf.8.en.html>.

- Отключить конфигурационный файл:

`sudo a2disconf {{configuration_file}}`

- Не показывать информационные сообщения:

`sudo a2disconf --quiet {{configuration_file}}`
