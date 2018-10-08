# gdb

> Отладчик от GNU.

- Запускает отладку исполняемого файла:

`gdb {{executable}}`

- Подключает процесс к gdb:

`gdb -p {{procID}}`

- Выполняет заданные команды GDB при старте:

`gdb -ex "{{commands}}" {{executable}}`

- Запускает gdb и передает аргументы:

`gdb --args {{executable}} {{argument1}} {{argument2}}`
