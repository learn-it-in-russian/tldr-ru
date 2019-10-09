# vncserver

> Запуск рабочего стола VNC (Virtual Network Computing).

- Запуск VNC-сервера на следующем доступном дисплее:

`vncserver`

- Запуск VNC-сервера с определенным разрешением экрана:

`vncserver --geometry {{width}}x{{height}}`

- Убить экземпляр VNC-сервера, запущенного на определенном дисплее:

`vncserver --kill :{{display_number}}`
