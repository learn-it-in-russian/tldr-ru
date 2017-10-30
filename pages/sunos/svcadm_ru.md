# svcadm

> Управление экземплярами служб.

- Включить службу в базе данных служб:

`svcadm enable {{service_name}}`

- Выключить службу:

`svcadm disable {{service_name}}`

- Перезапустить запущенную службу:

`svcadm restart {{service_name}}`

- Заставить службу перечитать конфигурационные файлы:

`svcadm refresh {{service_name}}`

- Вывести службу из режима "нуждается в обслуживании" и пеезапустить её:

`svcadm clear {{service_name}}`
