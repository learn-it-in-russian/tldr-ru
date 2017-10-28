# iptables

> Утилита для управления брандмауэром ядра Linux.

- Отобразить цепочки правил и отдельные правила для конкретной таблицы:

`sudo iptables -t {{table_name}} -vnL`

- Установить правило для цепочки правил:

`sudo iptables -p {{chain}} {{rule}}`

- Добавить правило в цепочку правил для IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Добавить правило в цепочку правил для IP, с учетом протокола и порта:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Удалить цепочку правил:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Сохранить конфигурацию iptables:

`sudo iptables-save > {{path/to/iptables_file}}`
