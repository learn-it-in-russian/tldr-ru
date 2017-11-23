# autossh

> Запускает, отслеживает и перезапускает SSH-подключения.
> Автоматическое переподключается для сохранения туннелей переадресации портов. Принимает все флаги ssh.

- Начинает сеанс SSH с перезапуском, когда порт мониторинг перестает возвращать данные:

`autossh -M {{monitor_port}} {{ssh_command}}`

- Начинает сеанс SSH с пробросом локального порта на удаленный, перезапуская, если нужно:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Делает форк (fork) запущенного прежде ssh (запускает в фоне) и не открывает удаленную оболочку:

`autossh -f -M {{monitor_port}} -N {{ssh_command}}`

- Запускает autossh в фоне без порта мониторинга, вместо этого проверяя соединение (keep-alive) каждые 10 секунд:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3"  {{ssh_command}}`

- Запускает autossh в фоне без порта мониторинга, удаленной оболочки, завершаясь, если не удается пробросить порт:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Запускает autossh в фоне с выводом отладочной информации в файл и подробным выводом журнала работы ssh во второй файл:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{log_file}} autossh -f -M {{monitor_port}} -v -E {{ssh_log_file}} {{ssh_command}}`
