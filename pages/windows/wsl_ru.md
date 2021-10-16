# wsl

> Управление подсистемой Windows для Linux в командной строке.
> Больше информации: <https://docs.microsoft.com/windows/wsl/reference>.

- Запустить команду в оболочке Linux по умолчанию:

`wsl {{shell_command}}`

- Запустить команду Linux без использования оболочки:

`wsl --exec {{command}} {{command_arguments}}`

- Запустить команду в определенном дистрибутиве:

`wsl --distribution {{distribution}} {{shell_command}}`

- Отобразить список установленных дистрибутивов:

`wsl --list`

- Экспортировать пользовательский образ WSL в `.tar` файл:

`wsl --export {{distribution}} {{path/to/distro_fs.tar}}`

- Импортировать пользовательский образ WSL из `.tar` файла:

`wsl --import {{distribution}} {{path/to/install_location}} {{path/to/distro_fs.tar}}`

- Указать версию WSL (1 или 2) для указанного дистрибутива:

`wsl --set-version {{distribution}} {{version}}`

- Выключить подсистему Windows для Linux:

`wsl --shutdown`
